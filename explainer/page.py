"""The report page: one self-contained HTML file with the decisions embedded as JSON.

Design notes (Apple's fluid-interface ideas, translated for the web): feedback on press, motion only on transform
and opacity, transitions that re-target from the current value so they can be interrupted, system font with
size-specific tracking, translucent chrome over content, and gentler variants for reduced motion, reduced
transparency and higher contrast.
"""

from __future__ import annotations

import json

from .verify import quoted_numbers

LOG_KEYS = {"gap_bps": "the gap in the log", "gap_vs_usual_offset_bps": "the gap against the usual offset, in the log",
            "model_ev_bps": "the model's expected value, in the log", "shown_usd": "the size shown, in the log",
            "quiet_s": "seconds the feed was quiet, in the log", "position_usd": "the position it would reach, in the log",
            "cap_usd": "the position cap, in the log", "fee_bps_per_leg": "the fee per leg, a setting of the run"}
COMPUTED_KEYS = {"both_legs_fees_bps": "two legs of fees (computed: 2 x fee per leg)",
                 "gap_after_fees_bps": "the gap against the offset minus both fees (computed)"}


def number_sources(text: str, facts: dict) -> list[dict]:
    """For each number in the text, the fact it matches and where that fact came from."""
    out = []
    for raw, val, dec in quoted_numbers(text):
        tol = 0.5 * 10 ** (-dec) + 1e-9
        src = None
        for k, label in {**LOG_KEYS, **COMPUTED_KEYS}.items():
            v = facts.get(k)
            if isinstance(v, (int, float)) and abs(abs(val) - abs(float(v))) <= tol:
                src = {"key": k, "label": label, "origin": "computed" if k in COMPUTED_KEYS else "log"}
                break
        out.append({"raw": raw, "value": val, "source": src})
    return out


def card_data(facts: dict, e) -> dict:
    return {"time": facts["time_utc"], "policy": facts["policy"], "action": facts["action"],
            "text": e.text, "writer": e.source, "verified": e.verified, "tries": e.tries,
            "reason": facts["reason_text"], "gap": facts["gap_bps"], "numbers": number_sources(e.text, facts)}


def render(cards: list[dict], summary: dict) -> str:
    return TEMPLATE.replace("__DATA__", json.dumps({"cards": cards, "summary": summary}).replace("</", "<\\/"))


TEMPLATE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>Why did it trade?</title>
<style>
:root{
  --bg:#fbfbfd; --surface:#fff; --ink:#1d1d1f; --mut:#6e6e73; --line:rgba(0,0,0,.08);
  --blue:#0071e3; --green:#1d8a4a; --amber:#b25e00; --chip:#f2f2f5;
  --nav:rgba(251,251,253,.72);
  --ease:cubic-bezier(.22,.8,.2,1);
}
@media (prefers-color-scheme:dark){:root{
  --bg:#000; --surface:#161618; --ink:#f5f5f7; --mut:#a1a1a6; --line:rgba(255,255,255,.1);
  --blue:#2997ff; --green:#30d158; --amber:#ff9f0a; --chip:#2a2a2d; --nav:rgba(22,22,24,.72);}}
@media (prefers-contrast:more){:root{--line:currentColor;--mut:var(--ink)}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);
  font:400 1.0625rem/1.5 -apple-system,BlinkMacSystemFont,"SF Pro Text",system-ui,sans-serif;
  -webkit-font-smoothing:antialiased;letter-spacing:-.011em}
a{color:var(--blue);text-decoration:none}
nav{position:sticky;top:0;z-index:10;display:flex;align-items:center;justify-content:space-between;gap:16px;
  padding:0 max(16px,calc((100vw - 980px)/2));height:48px;background:var(--nav);
  -webkit-backdrop-filter:saturate(180%) blur(20px);backdrop-filter:saturate(180%) blur(20px);
  border-bottom:1px solid var(--line);font-size:.8125rem}
nav b{font-weight:600;letter-spacing:-.01em} nav span{color:var(--mut)}
@media (prefers-reduced-transparency:reduce){nav{background:var(--bg);-webkit-backdrop-filter:none;backdrop-filter:none}}
main{max-width:980px;margin:0 auto;padding:0 16px 96px}
.hero{padding:88px 0 40px;text-align:center}
.eyebrow{font-size:1.0625rem;font-weight:600;color:var(--blue);letter-spacing:-.01em;margin:0 0 8px}
h1{font:700 clamp(2.5rem,8vw,5.5rem)/1.04 -apple-system,BlinkMacSystemFont,"SF Pro Display",system-ui,sans-serif;
  letter-spacing:-.035em;margin:0 0 20px}
.lede{font-size:clamp(1.1875rem,2.4vw,1.5rem);line-height:1.38;color:var(--mut);max-width:34ch;margin:0 auto;
  letter-spacing:-.015em}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:56px 0 0}
.stat{background:var(--surface);border-radius:22px;padding:28px 20px;text-align:center;border:1px solid var(--line)}
.stat .n{font:700 clamp(2.25rem,6vw,3.5rem)/1 -apple-system,system-ui,sans-serif;letter-spacing:-.03em;
  font-variant-numeric:tabular-nums}
.stat .l{color:var(--mut);font-size:.9375rem;margin-top:8px;line-height:1.35}
.sec{font:700 clamp(1.75rem,4vw,2.5rem)/1.1 -apple-system,system-ui,sans-serif;letter-spacing:-.03em;margin:72px 0 8px}
.sub{color:var(--mut);margin:0 0 24px;max-width:56ch}
.seg{position:relative;display:inline-flex;background:var(--chip);border-radius:10px;padding:2px;margin:0 0 20px;flex-wrap:wrap}
.seg button{position:relative;z-index:1;appearance:none;border:0;background:none;color:var(--ink);font:inherit;
  font-size:.875rem;font-weight:500;padding:6px 14px;border-radius:8px;cursor:pointer;
  transition:transform 120ms var(--ease)}
.seg button:active{transform:scale(.96)}
.seg .thumb{position:absolute;z-index:0;top:2px;bottom:2px;left:0;width:0;background:var(--surface);border-radius:8px;
  box-shadow:0 1px 3px rgba(0,0,0,.18),0 0 0 .5px var(--line);
  transition:transform 420ms var(--ease),width 420ms var(--ease)}
.card{background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:22px 24px;margin:12px 0;
  opacity:0;transform:translateY(14px);transition:opacity 500ms var(--ease),transform 500ms var(--ease)}
.card.in{opacity:1;transform:none}
.card.hide{display:none}
.top{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:.8125rem;color:var(--mut);margin-bottom:10px}
.pill{display:inline-flex;align-items:center;gap:6px;font-weight:600;font-size:.8125rem;padding:3px 10px 3px 8px;
  border-radius:99px;background:var(--chip)}
.pill i{width:8px;height:8px;border-radius:50%;background:var(--amber)}
.pill.ENTER i{background:var(--green)}
.card p.t{font-size:clamp(1.125rem,2.2vw,1.3125rem);line-height:1.46;letter-spacing:-.016em;margin:0}
mark{background:none;color:inherit;font-weight:600;border-bottom:1.5px solid color-mix(in srgb,var(--blue) 55%,transparent);
  cursor:help;position:relative;transition:background 150ms ease-out}
mark.src-computed{border-bottom-style:dashed}
mark.src-none{border-bottom-color:#d70015}
mark:hover,mark:focus-visible{background:color-mix(in srgb,var(--blue) 14%,transparent);outline:none}
mark[data-tip]::after{content:attr(data-tip);position:absolute;left:50%;bottom:calc(100% + 8px);
  transform:translate(-50%,4px);width:max-content;max-width:240px;background:var(--ink);color:var(--bg);
  font-size:.8125rem;font-weight:500;line-height:1.35;padding:7px 10px;border-radius:10px;pointer-events:none;
  opacity:0;transition:opacity 160ms ease-out,transform 160ms var(--ease);z-index:5;white-space:normal}
mark:hover::after,mark:focus-visible::after{opacity:1;transform:translate(-50%,0)}
details{margin-top:14px;color:var(--mut);font-size:.9375rem}
summary{cursor:pointer;color:var(--blue);list-style:none;display:inline-flex;gap:6px;align-items:center}
summary::-webkit-details-marker{display:none}
summary::after{content:"›";transition:transform 200ms var(--ease);display:inline-block}
details[open] summary::after{transform:rotate(90deg)}
.log{background:var(--chip);border-radius:12px;padding:12px 14px;margin-top:10px;
  font:.8125rem/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--ink);overflow-x:auto}
.checks{margin:10px 0 0;padding:0;list-style:none;display:grid;gap:4px}
.checks li{display:flex;gap:8px;align-items:baseline}
.checks b{color:var(--ink);font-variant-numeric:tabular-nums}
.ok{color:var(--green)}
.how{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:20px}
.how div{background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:22px}
.how b{display:block;font-size:1.0625rem;letter-spacing:-.015em;margin-bottom:6px}
.how span{color:var(--mut);font-size:.9375rem;line-height:1.45}
.how em{font-style:normal;color:var(--blue);font-weight:600}
footer{margin-top:64px;color:var(--mut);font-size:.8125rem;text-align:center;line-height:1.5}
@media (max-width:700px){.stats,.how{grid-template-columns:1fr}.hero{padding-top:56px}}
@media (prefers-reduced-motion:reduce){
  .card{transform:none;transition:opacity 200ms ease}
  .seg .thumb,summary::after,mark[data-tip]::after{transition:none}
  mark:hover::after,mark:focus-visible::after{transform:translate(-50%,0)}}
</style></head>
<body>
<nav><b>Why did it trade?</b><span>BTC · Binance vs Bybit · 19 Oct 2026</span></nav>
<main>
<section class="hero">
  <p class="eyebrow">A trading log, in plain English</p>
  <h1>Why did it trade?</h1>
  <p class="lede">An automated trader makes thousands of decisions a day. Here is each one, explained, with every number checked against the log.</p>
  <div class="stats" id="stats"></div>
</section>

<h2 class="sec">The decisions</h2>
<p class="sub">Hover a number to see where it came from. Solid underline: copied from the log. Dashed: computed from it.</p>
<div class="seg" id="seg" role="tablist" aria-label="Filter decisions"><span class="thumb"></span></div>
<div id="cards"></div>

<h2 class="sec">How the check works</h2>
<div class="how">
  <div><b>1. Facts only</b><span>The log line becomes a small set of facts. The writer gets nothing else, not even the time of day.</span></div>
  <div><b>2. Every number, checked</b><span>Each number in the answer must match a fact, rounding allowed. A skipped trade can't be called sent.</span></div>
  <div><b>3. <em>Fail</em> means retry</b><span>A bad answer goes back with the problem named. After two misses the plain template is shown instead.</span></div>
</div>
<footer id="foot"></footer>
</main>
<script>
const D = __DATA__;
const NAMES = {ENTER:"Sent", SKIP_EV:"Skipped: not worth it", SKIP_THIN:"Skipped: thin books",
  SKIP_STALE:"Skipped: quiet feed", SKIP_INVENTORY:"Skipped: position cap"};
const POL = {naive:"Naive policy", prior:"Fast decay prior", slow:"Slow model"};
const $ = (s, r=document) => r.querySelector(s);
const esc = s => s.replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

// stats
const S = D.summary;
$("#stats").innerHTML = [
  [S.total.toLocaleString(), "triggers, each judged by two policies"],
  [S.sent.toLocaleString(), "orders sent by the naive policy, which trades every gap"],
  [S.prior_sent.toLocaleString(), "orders sent by the fast prior, which prices fill risk"]
].map(([n,l]) => `<div class="stat"><div class="n">${n}</div><div class="l">${l}</div></div>`).join("");

// highlight numbers: walk the text, wrapping each matched number in <mark>
function mark(text, nums){
  let out = "", i = 0;
  for (const n of nums){
    const j = text.indexOf(n.raw, i);
    if (j < 0) continue;
    out += esc(text.slice(i, j));
    const tip = n.source ? `${n.raw}: ${n.source.label}` : "not found in the log";
    out += `<mark tabindex="0" class="${n.source ? "src-" + n.source.origin : "src-none"}" data-tip="${esc(tip)}">${esc(n.raw)}</mark>`;
    i = j + n.raw.length;
  }
  return out + esc(text.slice(i));
}

const wrap = $("#cards");
D.cards.forEach(c => {
  const el = document.createElement("article");
  el.className = "card"; el.dataset.action = c.action;
  const rows = c.numbers.filter(n => n.source).map(n =>
    `<li><span class="ok">✓</span><b>${esc(n.raw)}</b><span>${esc(n.source.label)}</span></li>`).join("");
  el.innerHTML = `
    <div class="top"><span class="pill ${c.action}"><i></i>${NAMES[c.action]}</span>
      <span>${esc(c.time)} UTC</span><span>${POL[c.policy] || esc(c.policy)}</span></div>
    <p class="t">${mark(c.text, c.numbers)}</p>
    <details><summary>Show the check</summary>
      <div class="log">${esc(c.reason)}  ·  gap ${c.gap} bps</div>
      <ul class="checks">${rows}</ul>
      <p style="margin:10px 0 0">Written by ${esc(c.writer)}${c.tries > 1 ? `, after ${c.tries} tries` : ", first try"}.</p>
    </details>`;
  wrap.appendChild(el);
});

// filter: a sliding thumb that re-targets from wherever it is
const seg = $("#seg"), thumb = $(".thumb", seg);
const kinds = ["ALL", ...Object.keys(NAMES).filter(k => D.cards.some(c => c.action === k))];
kinds.forEach(k => {
  const b = document.createElement("button");
  b.textContent = k === "ALL" ? "All" : NAMES[k].replace("Skipped: ", "Skipped · ");
  b.dataset.k = k; b.setAttribute("role", "tab");
  seg.appendChild(b);
});
function select(k){
  [...seg.querySelectorAll("button")].forEach(b => {
    const on = b.dataset.k === k; b.setAttribute("aria-selected", on);
    if (on){ thumb.style.width = b.offsetWidth + "px"; thumb.style.transform = `translateX(${b.offsetLeft - 2}px)`; }
  });
  document.querySelectorAll(".card").forEach(c => c.classList.toggle("hide", k !== "ALL" && c.dataset.action !== k));
  observe();
}
seg.addEventListener("pointerdown", e => { const b = e.target.closest("button"); if (b) select(b.dataset.k); });
seg.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " "){ const b = e.target.closest("button"); if (b) select(b.dataset.k); }});

// reveal cards as they scroll in
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); }}),
  {rootMargin:"0px 0px -8% 0px"});
function observe(){ document.querySelectorAll(".card:not(.in):not(.hide)").forEach(c => io.observe(c)); }

$("#foot").innerHTML = `${D.cards.length} of ${S.total.toLocaleString()} decisions shown, ${D.cards.filter(c => c.verified).length} verified.
  Replayed from our recording of 19 Oct 2026; no orders were sent anywhere.`;
requestAnimationFrame(() => select("ALL"));
addEventListener("resize", () => select([...seg.querySelectorAll("button")].find(b => b.getAttribute("aria-selected") === "true").dataset.k));
</script>
</body></html>
"""
