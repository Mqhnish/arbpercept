"""Explain a logged decision in plain English, and only with numbers that are in the log.

Writers share one rule (verify.py): a deterministic template, which needs nothing, and a model (Claude through
the API or the Claude Code CLI, or a free local model), which reads better. The model's text is checked; if it quotes a number that is not in the facts or reverses
the decision, it is asked again with the problem named, and after two failed tries the template is used.
Every explanation carries its source and whether it passed, so nothing unverified looks verified.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from .facts import POLICY_NAMES
from .verify import check

DEFAULT_MODEL = "claude-opus-5-5"
MAX_TRIES = 3  # the first answer and two corrections

SYSTEM = """You explain one decision made by an automated arbitrage trader to a student who has not seen the \
code. The trader watches the same coin on two exchanges and sometimes sees a price gap between them. For each \
gap it decides to trade, or to skip, and logs why.

Write two or three plain sentences. Say what the system saw, what it did, and the one reason that decided it. \
Rules:
- Use only numbers that appear in the facts JSON you are given, copied exactly or rounded. Never compute a new \
number, never estimate, never add a number from your own knowledge.
- Say clearly whether the trade was sent or skipped, in the same direction as the facts.
- Plain text only: no markdown, no dashes, no ellipses, and never correct yourself mid-sentence.
- Do not mention the time of day. Do not give investment advice. Do not call the decision good or bad.
- Quantities in basis points (bps): one bps is 0.01 percent of the trade's value."""


@dataclass
class Explanation:
    text: str
    source: str                      # the writer's name, "template", or "template (<writer> failed the check)"
    verified: bool
    tries: int = 0
    problems: list[str] = field(default_factory=list)


def template_explanation(f: dict) -> str:
    """A plain sentence built only from the facts. Always passes the check."""
    sell, buy = f["direction"].replace("sell ", "").split(" / buy ")
    offset = ""
    if abs(f["gap_bps"] - f["gap_vs_usual_offset_bps"]) > 1e-9:
        offset = f" ({f['gap_vs_usual_offset_bps']} bps once the usual offset between the two is removed)"
    head = f"{f['policy_name'].capitalize()} saw {sell} quoting {f['gap_bps']} bps above {buy}{offset}."
    a = f["action"]
    if a == "ENTER":
        tail = (f" It sent both orders. Fees on the two legs come to {f['both_legs_fees_bps']} bps, "
                f"which leaves {f['gap_after_fees_bps']} bps before fill risk.")
    elif a == "SKIP_EV":
        tail = (f" It skipped: the expected value after fees and the chance that only one leg fills was "
                f"{f['model_ev_bps']} bps, not positive.")
    elif a == "SKIP_THIN":
        tail = f" It skipped: the books showed only ${f['shown_usd']:,.0f} on both sides, too little to bother."
    elif a == "SKIP_STALE":
        tail = (f" It skipped: the {f['quiet_venue']} feed had been quiet for {f['quiet_s']} s, so the gap "
                f"could not be trusted.")
    else:
        tail = (f" It skipped: the trade would have taken the position to ${f['position_usd']:,.0f}, past the "
                f"${f['cap_usd']:,.0f} cap.")
    return head + tail


def build_prompt(facts: dict, feedback: str | None = None) -> str:
    content = "Facts:\n" + json.dumps({k: v for k, v in facts.items() if k != "reason_text"}, indent=1)
    if feedback:
        content += "\n\nYour previous answer failed a check: " + feedback + "\nWrite it again, fixing that."
    return content


class ClaudeAPIWriter:
    """Claude through the Anthropic API (needs an API key)."""
    name = "claude (API)"

    def __init__(self, client, model: str = DEFAULT_MODEL):
        self.client, self.model = client, model

    def __call__(self, facts: dict, feedback: str | None = None) -> str | None:
        resp = self.client.beta.messages.create(
            model=self.model,
            max_tokens=700,
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            output_config={"effort": "low"},
            system=SYSTEM,
            messages=[{"role": "user", "content": build_prompt(facts, feedback)}],
        )
        if resp.stop_reason == "refusal":
            return None
        return "".join(b.text for b in resp.content if b.type == "text").strip() or None


class ClaudeCLIWriter:
    """Claude through the Claude Code CLI (`claude -p`), which uses your Claude login, not an API key.
    Runs in an empty temporary directory with file and web tools switched off, so only the prompt is used."""
    name = "claude (CLI)"

    def __init__(self, model: str | None = None, binary: str = "claude", timeout: float = 180.0):
        self.model, self.binary, self.timeout = model, binary, timeout

    def __call__(self, facts: dict, feedback: str | None = None) -> str | None:
        import subprocess
        import tempfile
        cmd = [self.binary, "-p", build_prompt(facts, feedback), "--system-prompt", SYSTEM,
               "--no-session-persistence", "--disable-slash-commands",
               "--disallowedTools", "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,Task"]
        if self.model:
            cmd += ["--model", self.model]
        with tempfile.TemporaryDirectory() as tmp:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=self.timeout, cwd=tmp)
        return r.stdout.strip() or None if r.returncode == 0 else None


class OllamaWriter:
    """A free local model through Ollama (https://ollama.com): no account, no key, nothing leaves the machine."""
    name = "local model (Ollama)"

    def __init__(self, model: str = "llama3.2", host: str = "http://localhost:11434", timeout: float = 120.0):
        self.model, self.host, self.timeout = model, host, timeout

    def __call__(self, facts: dict, feedback: str | None = None) -> str | None:
        import requests
        r = requests.post(f"{self.host}/api/chat", timeout=self.timeout, json={
            "model": self.model, "stream": False, "options": {"temperature": 0},
            "messages": [{"role": "system", "content": SYSTEM},
                         {"role": "user", "content": build_prompt(facts, feedback)}]})
        r.raise_for_status()
        return r.json()["message"]["content"].strip() or None


class OpenAICompatWriter:
    """Any service with an OpenAI-style /chat/completions endpoint: Groq, Google Gemini, OpenRouter, a local
    server. Many have a free tier that needs an account but no card. The key is read from an environment
    variable and sent only to base_url."""

    def __init__(self, base_url: str, model: str, key_env: str = "LLM_API_KEY", timeout: float = 60.0):
        self.base_url, self.model, self.key_env, self.timeout = base_url.rstrip("/"), model, key_env, timeout
        self.name = f"{model} via {base_url.split('//')[-1].split('/')[0]}"

    def __call__(self, facts: dict, feedback: str | None = None) -> str | None:
        import os

        import requests
        key = os.environ.get(self.key_env)
        if not key:
            raise RuntimeError(f"set {self.key_env} to the service's API key")
        r = requests.post(f"{self.base_url}/chat/completions", timeout=self.timeout,
                          headers={"Authorization": f"Bearer {key}"},
                          json={"model": self.model, "temperature": 0, "max_tokens": 400,
                                "messages": [{"role": "system", "content": SYSTEM},
                                             {"role": "user", "content": build_prompt(facts, feedback)}]})
        r.raise_for_status()
        return (r.json()["choices"][0]["message"]["content"] or "").strip() or None


def explain(facts: dict, writer=None) -> Explanation:
    """The writer's explanation if it passes the check within MAX_TRIES, otherwise the template."""
    fallback = template_explanation(facts)
    if writer is None:
        return Explanation(fallback, "template", True, 0)
    problems: list[str] = []
    feedback = None
    for attempt in range(1, MAX_TRIES + 1):
        try:
            text = writer(facts, feedback)
        except Exception as e:  # noqa: BLE001 - a missing binary, a dead server, a network error: use the template
            problems.append(f"{writer.name} failed: {type(e).__name__}: {e}"[:200])
            break
        if text is None:
            problems.append(f"{writer.name} declined or returned nothing")
            break
        result = check(text, facts)
        if result["ok"]:
            return Explanation(text, writer.name, True, attempt, problems)
        bits = []
        if result["unsupported_numbers"]:
            bits.append("these numbers are not in the facts: " + ", ".join(result["unsupported_numbers"]))
        if result["wrong_action"]:
            bits.append(result["wrong_action"])
        if result["style"]:
            bits.append("; ".join(result["style"]))
        feedback = "; ".join(bits)
        problems.append(feedback)
    return Explanation(fallback, f"template ({writer.name} failed the check)", True, len(problems), problems)
