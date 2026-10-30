/* arbpercept dashboard: five views over /api. */
(function () {
  const $ = id => document.getElementById(id);
  const COLORS = { "naive fast path": "var(--s-naive)", "gap size only": "var(--s-gap)", "fast path + decay prior": "var(--s-prior)",
                   "slow model always": "var(--s-slow)", "latency-aware cascade": "var(--s-cascade)" };
  const BY_LABEL = { Naive: "naive fast path", "Gap size only": "gap size only", "Prior only": "fast path + decay prior",
                     "Slow always": "slow model always", Cascade: "latency-aware cascade" };
  const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  // ---- formatting ---------------------------------------------------------------------
  const MINUS = "−";
  function usd(v, signed = true) {
    if (v === null || v === undefined || !isFinite(v)) return "–";
    const a = Math.abs(v), s = a < 10 && a !== 0 ? a.toFixed(1) : Math.round(a).toLocaleString("en-US");
    if (s === "0" || s === "0.0") return "$0";
    return (v < 0 ? MINUS : signed ? "+" : "") + "$" + s;
  }
  function num(v, d = 1) { return v === null || v === undefined || !isFinite(v) ? "–" : (v < 0 ? MINUS : "") + Math.abs(v).toFixed(d); }
  function ci(lo, hi) {
    if (lo === null || hi === null) return "";
    const d = Math.max(Math.abs(lo), Math.abs(hi)) < 10 ? 1 : 0;
    const f = v => (v < 0 ? MINUS : "") + Math.abs(v).toFixed(d);
    return `[${f(lo)}, ${f(hi)}]`;
  }
  const sign = v => (v === null || v === undefined ? "" : v > 0 ? "pos" : v < 0 ? "neg" : "");
  const pct = v => (v === null || v === undefined ? "–" : Math.round(v * 100) + "%");
  const shortDate = d => { const [y, m, dd] = d.split("-"); return `${dd} ${MONTHS[+m - 1]} ’${y.slice(2)}`; };
  const monthYear = d => { const [y, m] = d.split("-"); return `${MONTHS[+m - 1]} ’${y.slice(2)}`; };
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const tagName = t => ({ "_v9_real": "v9 realistic: delayed-view births, closing split, run minimums",
                          "_tardis_real": "Tardis.dev ticks: 1st of each month, 2020–2026",
                          "_v7_real": "v7 realistic: 8 months, per-venue fees and latency, feed delay",
                          "_v6_real": "v6 realistic", "_v5_real": "v5 realistic", "_v5": "v5", "_v4_offset": "v4 offset-aware",
                          "_v3": "v3 raw gaps", "": "untagged" }[t] || t.replace(/^_/, ""));

  const VENUES = { binance: "Binance", bybit: "Bybit", okx: "OKX" };
  const venueName = v => VENUES[v] || v;
  // Coin, plus its venues when they are not the usual Binance and Bybit (the Tardis runs pair OKX too)
  const runLabel = r => r.coin + (r.venues && r.venues.join() !== "binance,bybit" ? ` ${r.venues.map(venueName).join("–")}` : "");

  // The static copy (python -m arbtrade.dashboard.export) has every GET answer saved as a file; this names
  // them the way api_file() in export.py does. It cannot take POSTs, so the paper trader stays local.
  const STATIC = document.documentElement.dataset.static === "1";
  function staticFile(path) {
    const u = new URL(path, "http://x"), q = Object.fromEntries(u.searchParams);
    if (u.pathname === "/api/run") return `api/run/${q.name}/${q.fee}_${q.tau}_${q.mode}_${q.cap}.json`;
    if (u.pathname === "/api/coins") return `api/coins/${q.tag}_${q.mode}_${q.cap}.json`;
    if (u.pathname === "/api/note") return `api/note/${q.path}.json`;
    return u.pathname.slice(1) + ".json";
  }

  async function api(path, body) {
    if (STATIC && body) throw new Error("This static copy cannot run the paper trader; run the dashboard locally.");
    if (STATIC) path = staticFile(path);
    const r = await fetch(path, body ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) } : {});
    if (STATIC && !r.ok) throw new Error(`not in this static copy: ${path}`);
    const j = await r.json();
    if (!r.ok) throw new Error(j.error || r.statusText);
    return j;
  }
  const store = {
    get(k, d) { try { const v = localStorage.getItem("arbpercept." + k); return v === null ? d : JSON.parse(v); } catch { return d; } },
    set(k, v) { try { localStorage.setItem("arbpercept." + k, JSON.stringify(v)); } catch { /* private window */ } },
  };

  function seg(id, onChange) {
    const box = $(id);
    const set = v => { box.dataset.value = v; for (const b of box.querySelectorAll("button")) b.classList.toggle("on", b.dataset.v === v); };
    set(box.dataset.value);
    box.addEventListener("click", e => { const b = e.target.closest("button"); if (b && b.dataset.v !== box.dataset.value) { set(b.dataset.v); onChange(b.dataset.v); } });
    return { get: () => box.dataset.value, set };
  }

  // ---- tabs -------------------------------------------------------------------------------
  const views = ["abstract", "figures", "results", "coins", "decay", "paper", "reports"];
  const HOME = "abstract";
  const loaded = {};  // view -> the promise of its first load
  // Links can carry settings after the view name: #coins?tag=_tardis_real&mode=conservative, #figures?f=btc
  function hashParams() {
    const h = location.hash.slice(1), i = h.indexOf("?");
    return i < 0 ? {} : Object.fromEntries(new URLSearchParams(h.slice(i + 1)));
  }
  async function route() {
    const name = (location.hash.replace("#", "").split("?")[0]) || HOME;
    const tab = views.includes(name) ? name : HOME;
    const shown = views.find(v => !$("view-" + v).hidden);
    for (const v of views) $("view-" + v).hidden = v !== tab;
    for (const a of document.querySelectorAll("#tabs a")) a.classList.toggle("on", a.dataset.tab === tab);
    Charts.hideTip();
    paper.visible = tab === "paper";
    if (shown !== tab) window.scrollTo(0, 0);
    const first = !loaded[tab];
    if (first) {
      loaded[tab] = ({ abstract: initAbstract, figures: initFigures, results: initResults, coins: initCoins, decay: initDecay,
                       paper: initPaper, reports: initReports })[tab]();
    }
    await loaded[tab];
    const q = hashParams(), apply = { figures: applyFigures, results: applyResults, coins: applyCoins, reports: applyReports }[tab];
    if (apply && Object.keys(q).length) apply(q, first);
  }
  window.addEventListener("hashchange", route);

  // ---- Abstract ---------------------------------------------------------------------------------
  // abstract.md is the abstract as submitted (docs/abstract/abstract.md). Links in it point at the views here;
  // the notes in the margin come from EVIDENCE, matched to each section by its heading.
  const EVIDENCE = [
    [/problem/i, [["img/survival.png", "How fast gaps close", "After 1 s most gaps are gone", "#figures?f=surv"]]],
    [/understanding/i, [["img/naive_v9.png", "Raw gaps are a trap", "Trading every gap loses money on every coin", "#figures?f=naive"],
                        ["§", "100 ms against 10 ms", "The resolution check behind the second trap", "#reports?p=resolution_check_BTC_2026-10-19.md"]]],
    [/approach/i, [["img/architecture.png", "The pipeline, explained", "Each stage and its measured cost", "#figures?f=arch"],
                   ["img/decay_auc.png", "Decay models", "AUC, calibration and survival", "#decay"]]],
    [/minimum/i, [["img/survival.png", "Decay report", "Survival curves and AUC from any run", "#decay"],
                  ["img/dashboard_paper.png", "Paper trader", "Every trigger, with the reason it traded or skipped", "#paper"]]],
    [/stretch/i, [["img/dashboard_paper.png", "Paper-trading demo", "Live books, simulated fills", "#paper"],
                  ["img/btc_cumulative_v9.png", "Latency in the replay", "Per-venue latency, fees and model time", "#results?run=btc_perp_binance_bybit_v9_real"]]],
    [/novelty/i, [["img/coins_v9.png", "Nine coins", "The cascade against the gap-size rule", "#figures?f=coins"],
                  ["img/naive_v9.png", "Trading every gap", "Loses $94 to $925 a day", "#figures?f=naive"]]],
    [/evaluation|results/i, [["img/btc_cumulative_v9.png", "BTC, 205 days", "Cumulative realised P&L", "#figures?f=btc"],
                             ["img/tardis_binance_bybit.png", "Tick data", "Both fill assumptions, three coins", "#figures?f=tardis"],
                             ["img/decay_auc.png", "Will the gap last?", "AUC with the 10 ms caveat", "#figures?f=auc"]]],
    [/feasibility|risk/i, [["{}", "Code and tests", "github.com/Mqhnish/arbpercept", "https://github.com/Mqhnish/arbpercept"],
                           ["§", "Every report", "The tables behind each number", "#reports"]]],
  ];
  function mdInline(s) {
    return esc(s)
      .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_, t, u) => `<a href="${u}"${/^https?:/.test(u.replace(/&amp;/g, "&")) ? ' target="_blank" rel="noopener"' : ""}>${t}</a>`)
      .replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>").replace(/(^|[\s(])_([^_]+)_(?=[\s.,;:)]|$)/g, "$1<i>$2</i>")
      .replace(/(^|[\s(])\*([^*]+)\*(?=[\s.,;:)]|$)/g, "$1<i>$2</i>").replace(/`([^`]+)`/g, "<code>$1</code>");
  }
  function renderAbstract(src) {
    const secs = [];
    let cur = null;
    const lines = src.split(/\r?\n/);
    for (let i = 0; i < lines.length; i++) {
      const l = lines[i].trim();
      if (!l) continue;
      if (l.startsWith("# ")) { $("a-title").innerHTML = esc(l.slice(2)).replace(/(\S+-\S+)/g, '<span class="nw">$1</span>'); continue; }
      if (l.startsWith("## ")) { cur = { title: l.slice(3), html: [] }; secs.push(cur); continue; }
      if (!cur) continue;  // the subtitle line: the hero already says it
      if (l.startsWith("### ")) { cur.html.push(`<h3>${mdInline(l.slice(4))}</h3>`); continue; }
      if (l === "[formula]") {
        cur.html.push('<p class="formula" role="math" aria-label="S of tau equals q of tau times e-hat minus c, plus one minus q of tau, times l-bar of tau">' +
                      "<i>S</i>(τ) = <i>q</i>(τ)·(<i>ê</i> − <i>c</i>) + (1 − <i>q</i>(τ))·<i>ℓ̄</i>(τ)</p>");
        continue;
      }
      if (l === "[architecture diagram]") {
        const cap = /^_.*_$/.test((lines[i + 1] || "").trim()) ? lines[++i].trim().slice(1, -1) : "";
        cur.html.push(`<figure><a href="#figures?f=arch"><img src="img/architecture.png" alt="The decision pipeline"></a>${cap ? `<figcaption>${mdInline(cap)}</figcaption>` : ""}</figure>`);
        continue;
      }
      if (l.startsWith("|") && /^\|[\s:|-]+\|$/.test((lines[i + 1] || "").trim())) {
        const cells = r => r.trim().replace(/^\||\|$/g, "").split("|").map(c => c.trim());
        let t = "<table><thead><tr>" + cells(l).map(c => `<th>${mdInline(c)}</th>`).join("") + "</tr></thead><tbody>";
        i += 2;
        while (i < lines.length && lines[i].trim().startsWith("|")) { t += "<tr>" + cells(lines[i]).map(c => `<td>${mdInline(c)}</td>`).join("") + "</tr>"; i++; }
        cur.html.push(t + "</tbody></table>"); i--; continue;
      }
      if (/^[-*]\s+/.test(l)) {
        let u = "<ul>";
        while (i < lines.length && /^[-*]\s+/.test(lines[i].trim())) { u += `<li>${mdInline(lines[i].trim().replace(/^[-*]\s+/, ""))}</li>`; i++; }
        cur.html.push(u + "</ul>"); i--; continue;
      }
      cur.html.push(`<p>${mdInline(l)}</p>`);
    }
    const card = ([img, t, n, href]) => `<a class="ev" href="${href}"${/^https?:/.test(href) ? ' target="_blank" rel="noopener"' : ""}>` +
      (img.startsWith("img/") ? `<img src="${img}" alt="" loading="lazy">` : `<span class="ev-glyph" aria-hidden="true">${esc(img)}</span>`) +
      `<span><b>${esc(t)}</b><span>${esc(n)}</span></span></a>`;
    $("a-body").innerHTML = secs.map(s => {
      const ev = (EVIDENCE.find(([re]) => re.test(s.title)) || [null, []])[1];
      return `<section class="ab-sec"><div class="ab-text"><h2>${mdInline(s.title)}</h2>${s.html.join("")}</div>` +
             `<aside class="ab-side">${ev.length ? '<p class="side-h">Evidence</p>' + ev.map(card).join("") : ""}</aside></section>`;
    }).join("");
  }
  async function initAbstract() {
    try {
      const r = await fetch("abstract.md");
      if (!r.ok) throw new Error(r.statusText);
      renderAbstract(await r.text());
    } catch (e) {
      $("a-body").innerHTML = `<p class="muted">Could not load the abstract (${esc(e.message)}).</p>`;
    }
  }

  // ---- Figures ----------------------------------------------------------------------------------
  function initFigures() {
    $("f-static-note").hidden = !STATIC;
    const sha = document.documentElement.dataset.commit;
    $("f-commit").innerHTML = sha ? `commit <a href="https://github.com/Mqhnish/arbpercept/commit/${esc(sha)}">${esc(sha)}</a>` : "the latest commit";
  }
  function applyFigures(q) {
    const el = $("f-" + q.f);
    if (!el) return;
    const still = document.hidden || matchMedia("(prefers-reduced-motion: reduce)").matches;
    requestAnimationFrame(() => el.scrollIntoView({ behavior: still ? "auto" : "smooth", block: "start" }));
    el.classList.remove("flash"); void el.offsetWidth; el.classList.add("flash");
  }

  // ---- Results ------------------------------------------------------------------------------
  let RUNS = [];
  const R = { sel: "latency-aware cascade", hidden: null, data: null };
  let rMode, rCap;

  async function initResults() {
    rMode = seg("r-mode", loadRun);
    rCap = seg("r-cap", loadRun);
    const q = hashParams();
    rMode.set(q.mode || store.get("mode", "optimistic"));
    rCap.set(q.cap || store.get("cap", "capped"));
    fillRunSelect();
    $("r-run").addEventListener("change", () => { setRunOptions(); loadRun(); });
    $("r-tau").addEventListener("change", loadRun);
    $("r-fee").addEventListener("change", loadRun);
    setRunOptions();
    await loadRun();
  }

  function fillRunSelect() {
    const sel = $("r-run");
    sel.innerHTML = "";
    const groups = {};
    for (const r of RUNS) (groups[r.tag] = groups[r.tag] || []).push(r);
    for (const tag of Object.keys(groups)) {
      const g = document.createElement("optgroup");
      g.label = tagName(tag);
      for (const r of groups[tag]) {
        const o = document.createElement("option");
        o.value = r.name;
        o.textContent = `${runLabel(r)} · ${r.days} days · ${monthYear(r.first)}–${monthYear(r.last)}`;
        g.appendChild(o);
      }
      sel.appendChild(g);
    }
    const want = (location.hash.match(/run=([^&]+)/) || [])[1] || store.get("run", null);
    if (want && RUNS.some(r => r.name === want)) sel.value = want;
  }

  function applyResults(q, first) {  // #results?run=..&mode=..&cap=.. (the first load already used them)
    if (first) return;
    let changed = false;
    if (q.run && q.run !== $("r-run").value && RUNS.some(r => r.name === q.run)) { $("r-run").value = q.run; setRunOptions(); changed = true; }
    if (q.mode && q.mode !== rMode.get()) { rMode.set(q.mode); changed = true; }
    if (q.cap && q.cap !== rCap.get()) { rCap.set(q.cap); changed = true; }
    if (changed) loadRun();
  }

  function setRunOptions() {
    const r = RUNS.find(x => x.name === $("r-run").value);
    if (!r) return;
    const fill = (id, vals, fmt, pick) => {
      const s = $(id); s.innerHTML = vals.map(v => `<option value="${v}">${fmt(v)}</option>`).join(""); s.value = String(pick);
    };
    fill("r-tau", r.taus, v => `${+v} ms`, r.taus.includes(50) ? 50 : r.taus[r.taus.length - 1]);
    fill("r-fee", r.fees, v => `${+v} bps/leg`, r.fees[0]);
    $("r-tau-wrap").hidden = r.taus.length < 2;
    $("r-fee-wrap").hidden = r.fees.length < 2;
    const lat = r.latencies_ms ? Object.values(r.latencies_ms)[0] : null;
    const bits = [];
    if (lat && lat[0] !== lat[1]) bits.push(`orders ${lat[0]}/${lat[1]} ms`);
    if (r.feed_delay_ms && r.feed_delay_ms.some(x => x)) bits.push(`feed delay ${r.feed_delay_ms.join("/")} ms`);
    bits.push(r.offset_aware ? "offset-aware" : "raw gaps");
    if (r.deplete_liquidity) bits.push("liquidity used up");
    bits.push(`${r.days} validation days`);
    $("r-setup").textContent = bits.join(" · ");
  }

  async function loadRun() {
    const name = $("r-run").value;
    if (!name) return;
    store.set("run", name); store.set("mode", rMode.get()); store.set("cap", rCap.get());
    const q = new URLSearchParams({ name, fee: $("r-fee").value, tau: $("r-tau").value, mode: rMode.get(), cap: rCap.get() });
    document.body.classList.add("busy");
    try {
      R.data = await api("/api/run?" + q);
    } catch (e) {
      $("r-kpis").innerHTML = `<div class="kpi"><span>Could not load this run</span><b>${esc(e.message)}</b></div>`;
      return;
    } finally {
      document.body.classList.remove("busy");
    }
    if (!R.data.strategies.some(s => s.key === R.sel)) R.sel = R.data.strategies[R.data.strategies.length - 1].key;
    renderResults();
  }

  function renderResults() {
    const d = R.data, S = Object.fromEntries(d.strategies.map(s => [s.key, s]));
    const casc = S["latency-aware cascade"], pair = (a, b) => d.pairs.find(p => p.a === a && p.b === b);
    const kp = [];
    if (casc) kp.push(["Cascade, per day", `<b class="${sign(casc.mean)}">${usd(casc.mean)}</b><i>${ci(casc.lo, casc.hi)}</i>`]);
    const g = pair("Cascade", "Gap size only"), n = pair("Cascade", "Naive"), sa = pair("Cascade", "Slow always");
    if (g) kp.push(["Edge over the gap-size rule", `<b class="${sign(g.lo > 0 ? 1 : g.hi < 0 ? -1 : 0)}">${usd(g.mean)}</b><i>${ci(g.lo, g.hi)}</i>`]);
    if (n) kp.push(["Edge over trading every gap", `<b>${usd(n.mean)}</b><i>${ci(n.lo, n.hi)}</i>`]);
    if (sa) kp.push(["Cascade − slow model always", `<b>${usd(sa.mean)}</b><i>${ci(sa.lo, sa.hi)}</i>`]);
    if (casc) kp.push(["Cascade: profitable days · trades/day", `<b>${pct(casc.win_days)}</b><i>${num(casc.trades_per_day)} trades</i>`]);
    kp.push(["Validation days", `<b>${d.days.length}</b><i>${d.days.length ? shortDate(d.days[0]) + " – " + shortDate(d.days[d.days.length - 1]) : ""}</i>`]);
    $("r-kpis").innerHTML = kp.map(([l, v]) => `<div class="kpi"><span>${l}</span>${v}</div>`).join("");

    // table
    const rows = d.strategies.map(s => `<tr data-k="${esc(s.key)}" class="${s.key === R.sel ? "sel" : ""}">
      <td><i class="sw" style="background:${COLORS[s.key]}"></i>${s.label}</td>
      <td class="n ${sign(s.mean)}">${usd(s.mean)}<span class="ci">${ci(s.lo, s.hi)}</span></td>
      <td class="n">${num(s.trades_per_day)}</td><td class="n">${pct(s.one_way)}</td></tr>`).join("");
    $("r-table").innerHTML = `<thead><tr><th>Strategy</th><th class="n">Realised $/day</th><th class="n">Trades</th><th class="n">One way</th></tr></thead><tbody>${rows}</tbody>`;
    $("r-table-foot").textContent = `${d.mode} fills · ${d.cap === "capped" ? "$50k position cap" : "no cap"} · ${+d.tau} ms · ${+d.fee} bps/leg average fee. "One way": share of trades that grow the same side.`;
    $("r-table").querySelectorAll("tbody tr").forEach(tr => tr.addEventListener("click", () => { R.sel = tr.dataset.k; renderResults(); }));
    const su = d.setup || {}, lat = su.latencies_ms ? Object.values(su.latencies_ms)[0] : null;
    const slow = su.slow_latency ? Object.values(su.slow_latency)[0] : null;
    const kv = [
      [`Fees, ${(d.venues || ["binance", "bybit"]).map(venueName).join(" / ")}`, su.venue_fees_bps ? `${su.venue_fees_bps[0]} / ${su.venue_fees_bps[1]} bps` : `${+d.fee} bps each`],
      ["Order latency", lat ? `${lat[0]} / ${lat[1]} ms` : `${+d.tau} ms`],
      ["Feed delay", su.feed_delay_ms ? `${su.feed_delay_ms[0]} / ${su.feed_delay_ms[1]} ms` : "none"],
      ["Gap measured against", su.offset_aware ? `trailing ${su.offset_window_s || 300} s offset` : "zero (raw gap)"],
      ["Displayed size", su.deplete_liquidity ? "used up by each fill" : "reused by every trigger"],
      ["Model inference", slow ? `prior ${(slow.fast_prior * 1000).toFixed(1)} µs · slow ${(slow.slow_model * 1000).toFixed(1)} µs` : "–"],
      ["Day end", su.close || "–"],
    ];
    $("r-setup-list").innerHTML = kv.map(([k, v]) => `<dt>${k}</dt><dd>${esc(v)}</dd>`).join("");

    // cumulative chart: naive starts hidden when its losses would flatten everything else
    if (R.hidden === null) {
      const end = s => Math.abs(s ? s.cum[s.cum.length - 1] || 0 : 0);
      R.hidden = new Set(S["naive fast path"] && casc && end(S["naive fast path"]) > 5 * Math.max(end(casc), 1) ? ["naive fast path"] : []);
    }
    $("r-legend").innerHTML = d.strategies.map(s => `<button data-k="${esc(s.key)}" class="${R.hidden.has(s.key) ? "off" : ""}"><i class="sw" style="background:${COLORS[s.key]}"></i>${s.label} <span class="mono ${sign(s.cum[s.cum.length - 1])}">${usd(s.cum[s.cum.length - 1])}</span></button>`).join("");
    $("r-legend").querySelectorAll("button").forEach(b => b.addEventListener("click", () => {
      R.hidden.has(b.dataset.k) ? R.hidden.delete(b.dataset.k) : R.hidden.add(b.dataset.k); renderResults();
    }));
    Charts.line($("r-cum"), {
      x: d.days, xFmt: monthYear, yFmt: v => usd(v, false), tipFmt: v => usd(v), vlines: d.fold_starts,
      tipTitle: i => shortDate(d.days[i]), includeZero: true,
      series: d.strategies.map(s => ({ label: s.label, color: COLORS[s.key], values: s.cum, hidden: R.hidden.has(s.key),
                                       width: s.key === "latency-aware cascade" ? 2.2 : 1.4 })),
    });

    // selected strategy: daily bars and composition
    const s = S[R.sel];
    $("r-sel-name").textContent = s.label;
    $("r-daily-hint").textContent = `best ${usd(s.best_day)} · worst ${usd(s.worst_day)} · ${pct(s.win_days)} of days above $0`;
    Charts.bars($("r-daily"), { x: d.days, values: s.daily, xFmt: monthYear, yFmt: v => usd(v, false), tipFmt: v => usd(v) });
    $("r-parts-hint").textContent = `${s.label}, $/day`;
    Charts.hbars($("r-parts"), { fmt: v => usd(v), rows: [
      { label: "Trades", value: s.parts.trades }, { label: "Funding", value: s.parts.funding },
      { label: "Closing", value: s.parts.close }, { label: "Net", value: s.mean, color: "var(--ink)" }] });
    Charts.forest($("r-pairs"), { labelWidth: 112, xFmt: v => usd(v), rows: d.pairs.filter(p => p.b !== "Naive").map(p => ({
      label: `${p.a} − ${p.b}`.replace("Gap size only", "Gap rule").replace("Slow always", "Slow"), mean: p.mean, lo: p.lo, hi: p.hi,
      color: p.lo > 0 ? "var(--pos)" : p.hi < 0 ? "var(--neg)" : "var(--ink-2)",
      tip: `${p.a} − ${p.b}: ${usd(p.mean)} ${ci(p.lo, p.hi)} per day` })) });

    // P&L against latency, when there are several
    $("r-tau-panel").hidden = !d.by_tau.length;
    if (d.by_tau.length) {
      const taus = d.by_tau[0].points.map(p => p.tau);
      Charts.line($("r-bytau"), { x: taus, numericX: true, logX: taus[taus.length - 1] / Math.max(taus[0], 0.1) > 20, dots: true,
        xFmt: v => `${+v} ms`, yFmt: v => usd(v, false), tipFmt: v => usd(v), includeZero: true, tipTitle: i => `${+taus[i]} ms`,
        series: d.by_tau.map(s => ({ label: s.label, color: COLORS[s.key], values: s.points.map(p => p.mean), hidden: R.hidden.has(s.key) })) });
    }
  }

  // ---- Coins ---------------------------------------------------------------------------------
  let cMode, cCap;
  async function initCoins() {
    cMode = seg("c-mode", loadCoins);
    cCap = seg("c-cap", loadCoins);
    const tags = [...new Set(RUNS.map(r => r.tag))].filter(t => RUNS.filter(r => r.tag === t).length > 1);
    $("c-tag").innerHTML = tags.map(t => `<option value="${esc(t)}">${esc(tagName(t))}</option>`).join("");
    $("c-tag").addEventListener("change", loadCoins);
    const q = hashParams();
    if (q.tag && tags.includes(q.tag)) $("c-tag").value = q.tag;
    if (q.mode) cMode.set(q.mode);
    if (q.cap) cCap.set(q.cap);
    await loadCoins();
  }
  function applyCoins(q, first) {  // #coins?tag=..&mode=..&cap=..
    if (first) return;
    let changed = false;
    if (q.tag && q.tag !== $("c-tag").value && [...$("c-tag").options].some(o => o.value === q.tag)) { $("c-tag").value = q.tag; changed = true; }
    if (q.mode && q.mode !== cMode.get()) { cMode.set(q.mode); changed = true; }
    if (q.cap && q.cap !== cCap.get()) { cCap.set(q.cap); changed = true; }
    if (changed) loadCoins();
  }
  async function loadCoins() {
    const q = new URLSearchParams({ tag: $("c-tag").value, mode: cMode.get(), cap: cCap.get() });
    const d = await api("/api/coins?" + q);
    const open = run => { location.hash = "results?run=" + run; $("r-run").value = run; setRunOptions(); loadRun(); };
    const wide = d.rows.some(r => runLabel(r) !== r.coin);
    Charts.forest($("c-forest"), { labelWidth: wide ? 120 : 56, xFmt: v => usd(v), onClick: r => { loaded.results ? open(r.run) : (store.set("run", r.run), location.hash = "results"); },
      rows: d.rows.map(r => { const c = r.strategies.Cascade || {}, g = r.strategies["Gap size only"];
        return { label: runLabel(r), run: r.run, mean: c.mean ?? null, lo: c.lo, hi: c.hi,
                 color: c.lo > 0 ? "var(--s-cascade)" : c.hi < 0 ? "var(--neg)" : "var(--ink-2)", alt: g,
                 tip: `${r.coin}: cascade ${usd(c.mean)} ${ci(c.lo, c.hi)}${g ? `, gap rule ${usd(g.mean)} ${ci(g.lo, g.hi)}` : ""} per day, ${r.days} days` }; }) });
    const cell = (c, withCi = true) => c ? `<span class="${sign(c.mean)}">${usd(c.mean)}</span>${withCi ? `<span class="ci">${ci(c.lo, c.hi)}</span>` : ""}` : "–";
    const go = run => { store.set("run", run); if (loaded.results) open(run); else location.hash = "results?run=" + run; };
    $("c-table").innerHTML = `<thead><tr><th>Coin</th><th class="n">Days</th><th>Period</th><th class="n">Naive</th><th class="n">Gap rule</th>
      <th class="n">Cascade</th><th class="n">Cascade − gap rule</th><th class="n">Trades</th></tr></thead><tbody>${d.rows.map(r => `
      <tr data-run="${esc(r.run)}"><td><b>${esc(runLabel(r))}</b></td><td class="n">${r.days}</td><td class="muted">${r.first ? monthYear(r.first) + "–" + monthYear(r.last) : ""}</td>
      <td class="n">${cell(r.strategies.Naive, false)}</td><td class="n">${cell(r.strategies["Gap size only"])}</td>
      <td class="n">${cell(r.strategies.Cascade)}</td><td class="n">${cell(r.edge_vs_gap)}</td><td class="n">${num(r.trades_per_day)}</td></tr>`).join("")}</tbody>`;
    $("c-table").querySelectorAll("tbody tr").forEach(tr => tr.addEventListener("click", () => go(tr.dataset.run)));
    const beat = d.rows.filter(r => r.edge_vs_gap && r.edge_vs_gap.lo > 0).length;
    const pos = d.rows.filter(r => r.strategies.Cascade && r.strategies.Cascade.lo > 0).length;
    $("c-foot").textContent = `${pos} of ${d.rows.length} coins have a cascade interval above $0; on ${beat} the cascade beats the gap-size rule on the same days. Naive shows the mean only. Trades: cascade trades per day.`;
    $("c-minis").innerHTML = d.rows.map((r, i) => `<div class="mini" data-run="${esc(r.run)}"><div class="h"><b>${esc(runLabel(r))}</b>
      <span class="mono ${sign((r.cum.Cascade || []).slice(-1)[0])}">${usd((r.cum.Cascade || []).slice(-1)[0])}</span></div><div class="chart" id="c-mini-${i}"></div></div>`).join("");
    d.rows.forEach((r, i) => {
      Charts.line($("c-mini-" + i), { x: r.dates, compact: true, yFmt: v => usd(v, false), tipFmt: v => usd(v), includeZero: true,
        tipTitle: j => `${r.coin}, ${shortDate(r.dates[j])}`,
        series: [{ label: "Gap rule", color: "var(--s-gap)", values: r.cum["Gap size only"] || [], width: 1 },
                 { label: "Cascade", color: "var(--s-cascade)", values: r.cum.Cascade || [], width: 1.6 }] });
    });
    $("c-minis").querySelectorAll(".mini").forEach(m => m.addEventListener("click", () => go(m.dataset.run)));
  }

  // ---- Decay ---------------------------------------------------------------------------------
  const DCOL = { "all features (gradient boosting, calibrated)": "var(--s-cascade)", "all features (gradient boosting)": "var(--s-slow)",
                 "all features (logistic)": "var(--s-prior)", "gap size only (logistic)": "var(--s-gap)",
                 "survival rate only (Kaplan-Meier style)": "var(--ink-3)" };
  let DEC, dBirths;
  async function initDecay() {
    DEC = await api("/api/decay");
    if (!DEC.rows.length) { $("d-auc").innerHTML = '<p class="empty">No decay summary in data/reports/decay.</p>'; return; }
    $("d-source").textContent = `data/reports/decay/${DEC.source} · walk-forward folds, development days only`;
    const pairs = [...new Set(DEC.rows.map(r => r.pair))];
    $("d-pair").innerHTML = pairs.map(p => `<option>${p}</option>`).join("");
    dBirths = seg("d-births", renderDecay);
    $("d-pair").addEventListener("change", () => { fillHurdles(); renderDecay(); });
    $("d-hurdle").addEventListener("change", renderDecay);
    fillHurdles(); renderDecay();
  }
  function fillHurdles() {
    const hs = [...new Set(DEC.rows.filter(r => r.pair === $("d-pair").value).map(r => r.hurdle))];
    $("d-hurdle").innerHTML = hs.map(h => `<option>${h}</option>`).join("");
  }
  function renderDecay() {
    const rows = DEC.rows.filter(r => r.pair === $("d-pair").value && r.births === dBirths.get() && r.hurdle === $("d-hurdle").value);
    const taus = [...new Set(rows.map(r => r.tau_ms))].sort((a, b) => a - b);
    const models = [...new Set(rows.map(r => r.model))].filter(m => !m.startsWith("survival"));
    $("d-legend").innerHTML = models.map(m => `<span><i class="sw" style="background:${DCOL[m] || "var(--ink-2)"}"></i>${m}</span>`).join("");
    Charts.line($("d-auc"), { x: taus, numericX: true, dots: true, xFmt: v => `${v} ms`, yFmt: v => v.toFixed(2), hline: 0.5,
      tipTitle: i => `τ = ${taus[i]} ms`, empty: "No rows for this choice",
      series: models.map(m => ({ label: m, color: DCOL[m] || "var(--ink-2)", width: m.includes("calibrated") ? 2.2 : 1.4,
        values: taus.map(t => { const r = rows.find(x => x.model === m && x.tau_ms === t); return r ? r.auc : null; }) })) });
    const body = [];
    for (const t of taus) for (const m of models) {
      const r = rows.find(x => x.model === m && x.tau_ms === t);
      if (!r) continue;
      body.push(`<tr><td class="n">${t}</td><td><i class="sw" style="background:${DCOL[m] || "var(--ink-2)"}"></i>${m.replace("all features ", "").replace(/[()]/g, "")}</td>
        <td class="n">${r.auc.toFixed(3)}<span class="ci">±${(r.auc_sd || 0).toFixed(3)}</span></td><td class="n">${num(r.bss, 3)}</td><td class="n">${num(r.ece, 3)}</td><td class="n">${pct(r.alive)}</td></tr>`);
    }
    renderSurvival();
    $("d-table").innerHTML = `<thead><tr><th class="n">τ ms</th><th>Model</th><th class="n">AUC</th><th class="n">Brier skill</th><th class="n">ECE</th><th class="n">Open</th></tr></thead><tbody>${body.join("")}</tbody>`;
  }

  const SCOL = ["var(--s-prior)", "var(--s-naive)", "var(--s-cascade)", "var(--s-slow)"];
  function renderSurvival() {
    const sv = DEC.survival;
    $("d-surv-panel").hidden = !sv;
    if (!sv) return;
    const hs = Object.keys(sv.curves), t = sv.curves[hs[0]].t;
    $("d-surv-hint").textContent = `${sv.pair || "one pair"}, fresh-quote births, development days. Band: what 100 ms sampling allows, from surely open to possibly open.`;
    $("d-surv-legend").innerHTML = hs.map((h, i) => `<span><i class="sw" style="background:${SCOL[i % 4]}"></i>${h} · ${sv.curves[h].n.toLocaleString()} births</span>`).join("");
    Charts.line($("d-surv"), { x: t, numericX: true, logX: true, xFmt: v => (v >= 1000 ? `${(v / 1000).toFixed(1)} s` : `${Math.round(v)} ms`), yMin: 0, yMax: 1,
      yFmt: v => Math.round(v * 100) + "%", tipFmt: v => (v * 100).toFixed(1) + "%", tipTitle: i => `${Math.round(t[i])} ms after birth`, xTickCount: 8,
      series: hs.map((h, i) => ({ label: h + ", surely open", color: SCOL[i % 4], values: sv.curves[h].lo, band: { lo: sv.curves[h].lo, hi: sv.curves[h].hi } })) });
  }

  // ---- Paper trader ------------------------------------------------------------------------------
  const paper = { visible: false, timer: null, last: null };
  let pSource;
  function initPaper() {
    if (STATIC) { $("p-static").hidden = false; $("p-live").hidden = true; return; }
    pSource = seg("p-source", v => {
      document.querySelectorAll(".only-live").forEach(e => (e.hidden = v !== "live"));
      document.querySelectorAll(".only-replay").forEach(e => (e.hidden = v !== "replay"));
    });
    $("p-start").addEventListener("click", async () => {
      const body = { source: pSource.get(), asset: $("p-asset").value, minutes: +$("p-minutes").value, date: $("p-date").value,
                     speed: $("p-speed").value, fee: +$("p-fee").value, offset_window_s: +$("p-window").value,
                     lat_binance: +$("p-lat-bn").value, lat_bybit: +$("p-lat-by").value };
      try { await api("/api/paper/start", body); } catch (e) { $("p-status").textContent = e.message; }
      pollPaper();
    });
    $("p-stop").addEventListener("click", async () => { await api("/api/paper/stop", {}); pollPaper(); });
    pollPaper();
  }
  async function pollPaper() {
    clearTimeout(paper.timer);
    let s;
    try { s = await api("/api/paper"); } catch { s = { status: "unavailable" }; }
    renderPaper(s);
    const live = s.status === "running" || s.status === "starting";
    paper.timer = setTimeout(pollPaper, live && paper.visible ? 1000 : 4000);
  }
  function renderPaper(s) {
    const running = s.status === "running" || s.status === "starting";
    $("p-start").disabled = running; $("p-stop").disabled = !running;
    $("p-status").innerHTML = `<span class="status-dot ${s.status}"></span>${esc(s.status || "idle")}`;
    if (s.error) $("p-note").innerHTML = `<span class="neg">${esc(s.error)}</span>`;
    else if (s.note) $("p-note").textContent = s.note;
    const b = s.books || {}, g = s.gaps || {}, trig = s.trigger_bps;
    const book = (name, q) => `<div><h3>${name}</h3>${q && q.bid !== null ? `<div class="quote">
      <span class="k">bid</span><span>${q.bid.toFixed(2)}</span><span class="muted">${num(q.bid_sz, 3)}</span>
      <span class="k">ask</span><span>${q.ask.toFixed(2)}</span><span class="muted">${num(q.ask_sz, 3)}</span>
      <span class="k">age</span><span>${q.age_ms === null ? "–" : Math.round(q.age_ms) + " ms"}</span><span></span></div>` : '<p class="muted">no quote yet</p>'}</div>`;
    const gl = (label, v) => `<span class="k">${label}</span><span class="${v !== null && v !== undefined && trig && v > trig ? "pos" : ""}">${v === null || v === undefined ? "–" : num(v, 2)}</span><span class="muted">bps</span>`;
    $("p-books").innerHTML = book("Binance", b.binance) + book("Bybit", b.bybit) +
      `<div><h3>Gap against the usual offset</h3><div class="quote">${gl("sell Binance", g.sell_a)}${gl("sell Bybit", g.sell_b)}${gl("offset", g.offset)}
       <span class="k">trigger</span><span>${trig ? num(trig, 2) : "–"}</span><span class="muted">bps</span></div></div>` +
      `<div><h3>Session</h3><div class="big">${s.triggers ?? 0}<span class="hint"> triggers</span></div>
       <div class="hint">${s.events ? s.events.toLocaleString() + " quotes · " + fmtDur(s.market_elapsed_s) + " of market" : "not started"}${s.source ? " · " + s.source : ""}</div>
       ${s.widest ? `<div class="hint">widest gap seen: ${num(s.widest.sell_a, 2)} / ${num(s.widest.sell_b, 2)} bps</div>` : ""}</div>`;
    const h = s.history || [];
    Charts.line($("p-gap"), { x: h.map(p => p.t), xTickPx: 120, xFmt: t => new Date(t).toISOString().slice(11, 19), yFmt: v => num(v, 1),
      tipTitle: i => new Date(h[i].t).toISOString().slice(11, 23) + " UTC", hline: trig, empty: "Start a session to see the gap",
      series: [{ label: "sell Binance / buy Bybit", color: "var(--s-prior)", values: h.map(p => p.sell_a) },
               { label: "sell Bybit / buy Binance", color: "var(--s-naive)", values: h.map(p => p.sell_b) }] });
    const sum = s.summary || {};
    $("p-policies").innerHTML = `<thead><tr><th>Policy</th><th class="n">Trades</th><th class="n">Full fills</th><th class="n">P&amp;L</th><th class="n">Position</th><th>Skipped</th></tr></thead><tbody>${
      Object.entries(sum).map(([k, v]) => { const pos = Object.entries(v).find(([kk]) => kk.startsWith("position_on_")); const dec = v.decisions || {};
        const skips = Object.entries(dec).filter(([a]) => a.startsWith("SKIP")).map(([a, c]) => `${a.slice(5).toLowerCase()} ${c}`).join(", ");
        return `<tr><td>${k}</td><td class="n">${v.trades}</td><td class="n">${v.full_fills}</td><td class="n ${sign(v.pnl_usd)}">${usd(v.pnl_usd)}</td><td class="n">${pos ? num(pos[1], 4) : "–"}</td><td class="muted">${skips || "–"}</td></tr>`; }).join("") ||
      '<tr><td colspan="6" class="muted">No session yet.</td></tr>'}</tbody>`;
    const dec = s.decisions || [];
    $("p-decisions").innerHTML = `<thead><tr><th>Time (UTC)</th><th>Policy</th><th>Direction</th><th class="n">Gap</th><th>Action</th><th>Reason</th></tr></thead><tbody>${
      dec.map(x => `<tr><td class="mono">${new Date(x.t / 1000).toISOString().slice(11, 23)}</td><td>${x.policy}</td><td>${esc(x.direction)}</td>
        <td class="n">${num(x.edge_rel_bps ?? x.edge_bps, 2)}</td><td><span class="tag ${x.action === "ENTER" ? "enter" : "skip"}">${x.action}</span></td><td class="muted">${esc(x.reason)}</td></tr>`).join("") ||
      '<tr><td colspan="6" class="muted">Decisions appear here when a gap opens past the trigger.</td></tr>'}</tbody>`;
  }
  const fmtDur = s => (s < 120 ? `${Math.round(s)} s` : s < 7200 ? `${(s / 60).toFixed(1)} min` : `${(s / 3600).toFixed(1)} h`);

  // ---- Reports -----------------------------------------------------------------------------------
  async function initReports() {
    const files = await api("/api/notes");
    $("n-list").innerHTML = files.map(f => `<li data-p="${esc(f.path)}" title="${esc(f.path)}">${esc(f.path)}</li>`).join("");
    $("n-list").querySelectorAll("li").forEach(li => li.addEventListener("click", () => openNote(li.dataset.p)));
    const want = hashParams().p;
    const first = files.find(f => f.path === want) || files.find(f => /btc_perp_binance_bybit_v9_real\/inventory/.test(f.path)) ||
                  files.find(f => f.path.includes("inventory")) || files[0];
    if (first) openNote(first.path);
  }
  function applyReports(q, first) { if (!first && q.p) openNote(q.p); }  // #reports?p=<path in data/reports>
  async function openNote(p) {
    const li = [...$("n-list").querySelectorAll("li")].find(x => x.dataset.p === p);
    $("n-list").querySelectorAll("li").forEach(x => x.classList.toggle("sel", x === li));
    if (li) li.scrollIntoView({ block: "nearest" });
    const d = await api("/api/note?" + new URLSearchParams({ path: p }));
    $("n-body").innerHTML = md(d.text);
  }
  function md(src) {
    const inline = s => esc(s).replace(/`([^`]+)`/g, "<code>$1</code>").replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>")
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, "$1");
    const out = [], lines = src.split(/\r?\n/);
    for (let i = 0; i < lines.length; i++) {
      const l = lines[i];
      if (/^\|/.test(l) && i + 1 < lines.length && /^\|[\s:|-]+\|$/.test(lines[i + 1].trim())) {
        const cells = r => r.trim().replace(/^\||\|$/g, "").split("|").map(c => c.trim());
        let html = "<table><thead><tr>" + cells(l).map(c => `<th>${inline(c)}</th>`).join("") + "</tr></thead><tbody>";
        i += 2;
        while (i < lines.length && /^\|/.test(lines[i])) { html += "<tr>" + cells(lines[i]).map(c => `<td>${inline(c)}</td>`).join("") + "</tr>"; i++; }
        out.push(html + "</tbody></table>"); i--; continue;
      }
      const h = l.match(/^(#{1,3})\s+(.*)/);
      if (h) { out.push(`<h${h[1].length}>${inline(h[2])}</h${h[1].length}>`); continue; }
      if (/^\s*[-*]\s+/.test(l)) {
        let html = "<ul>";
        while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) { html += `<li>${inline(lines[i].replace(/^\s*[-*]\s+/, ""))}</li>`; i++; }
        out.push(html + "</ul>"); i--; continue;
      }
      if (l.trim()) out.push(`<p>${inline(l)}</p>`);
    }
    return out.join("\n");
  }

  // ---- start ----------------------------------------------------------------------------------------
  (async function boot() {
    try { RUNS = await api("/api/runs"); } catch (e) { RUNS = []; }
    $("meta").textContent = `${RUNS.length} runs in data/reports${STATIC ? " · static copy" : ""}`;
    if (!location.hash) history.replaceState(null, "", "#" + HOME);
    route();
  })();
})();
