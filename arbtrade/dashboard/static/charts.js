/* Small SVG charts: line (with crosshair), bars, forest (estimate + interval), signed bars.
   No library: each chart redraws from its last arguments when its box changes size. */
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const tip = () => document.getElementById("tip");

  function el(name, attrs, parent) {
    const e = document.createElementNS(NS, name);
    for (const k in attrs) if (attrs[k] !== undefined && attrs[k] !== null) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }

  function niceTicks(lo, hi, n) {
    if (!isFinite(lo) || !isFinite(hi)) return { lo: 0, hi: 1, ticks: [0, 1] };
    if (lo === hi) { lo -= 1; hi += 1; }
    const span = hi - lo;
    let step = Math.pow(10, Math.floor(Math.log10(span / n)));
    const err = (n / span) * step;
    if (err <= 0.15) step *= 10; else if (err <= 0.35) step *= 5; else if (err <= 0.75) step *= 2;
    const a = Math.floor(lo / step) * step, b = Math.ceil(hi / step) * step;
    const ticks = [];
    for (let v = a; v <= b + step / 2; v += step) ticks.push(Math.abs(v) < step / 1e6 ? 0 : v);
    return { lo: a, hi: b, ticks };
  }

  function frame(host) {
    host.innerHTML = "";
    const w = host.clientWidth || 300, h = host.clientHeight || 200;
    const svg = el("svg", { viewBox: `0 0 ${w} ${h}`, preserveAspectRatio: "none" }, host);
    return { svg, w, h };
  }

  function showTip(html, ev) {
    const t = tip();
    t.innerHTML = html;
    t.hidden = false;
    const pad = 14, r = t.getBoundingClientRect();
    let x = ev.clientX + pad, y = ev.clientY + pad;
    if (x + r.width > window.innerWidth - 4) x = ev.clientX - r.width - pad;
    if (y + r.height > window.innerHeight - 4) y = ev.clientY - r.height - pad;
    t.style.left = x + "px"; t.style.top = y + "px";
  }
  const hideTip = () => { tip().hidden = true; };

  const registry = new Map();
  const ro = new ResizeObserver(entries => {
    for (const e of entries) {
      const job = registry.get(e.target);
      if (job && (e.contentRect.width !== job.w)) { job.w = e.contentRect.width; job.fn(); }
    }
  });
  function remember(host, fn) {
    if (!registry.has(host)) ro.observe(host);
    registry.set(host, { fn, w: host.clientWidth });
  }

  /* line: x = labels (index scale) or numbers (opts.numericX, optional log scale).
     series: [{label, color, values, dash, width, band: {lo:[], hi:[]}}] */
  function line(host, opts) {
    remember(host, () => line(host, opts));
    const { svg, w, h } = frame(host);
    const m = opts.compact ? { l: 2, r: 2, t: 4, b: 4 } : { l: 50, r: 12, t: 8, b: 22 };
    const xs = opts.x, n = xs.length;
    const shown = opts.series.filter(s => !s.hidden);
    if (!n || !shown.length) { el("text", { x: w / 2, y: h / 2, "text-anchor": "middle", class: "lbl" }, svg).textContent = opts.empty || "No data"; return; }
    let lo = Infinity, hi = -Infinity;
    for (const s of shown) {
      for (const v of s.values) if (v !== null && isFinite(v)) { lo = Math.min(lo, v); hi = Math.max(hi, v); }
      if (s.band) for (const k of ["lo", "hi"]) for (const v of s.band[k]) if (v !== null && isFinite(v)) { lo = Math.min(lo, v); hi = Math.max(hi, v); }
    }
    if (opts.hline !== undefined && opts.hline !== null) { lo = Math.min(lo, opts.hline); hi = Math.max(hi, opts.hline); }
    if (opts.includeZero) { lo = Math.min(lo, 0); hi = Math.max(hi, 0); }
    if (opts.yMin !== undefined) lo = opts.yMin;
    if (opts.yMax !== undefined) hi = opts.yMax;
    const yt = niceTicks(lo, hi, Math.max(3, Math.round((h - m.t - m.b) / 45)));
    const Y = v => m.t + (h - m.t - m.b) * (1 - (v - yt.lo) / (yt.hi - yt.lo));
    let X;
    if (opts.numericX) {
      const lg = opts.logX, f = v => (lg ? Math.log10(v) : v);
      const a = f(Math.min(...xs)), b = f(Math.max(...xs));
      X = i => m.l + (w - m.l - m.r) * (b === a ? 0.5 : (f(xs[i]) - a) / (b - a));
    } else {
      X = i => m.l + (w - m.l - m.r) * (n === 1 ? 0.5 : i / (n - 1));
    }

    const ax = el("g", { class: "ax" }, svg);
    if (opts.compact) {
      if (yt.lo < 0 && yt.hi > 0) el("line", { x1: m.l, x2: w - m.r, y1: Y(0), y2: Y(0), class: "zero" }, svg);
    } else {
      for (const v of yt.ticks) {
        el("line", { x1: m.l, x2: w - m.r, y1: Y(v), y2: Y(v), class: v === 0 ? "zero" : "grid-l" }, svg);
        el("text", { x: m.l - 6, y: Y(v) + 3.5, "text-anchor": "end" }, ax).textContent = (opts.yFmt || String)(v);
      }
      const kx = Math.max(2, Math.floor((w - m.l - m.r) / (opts.xTickPx || 80)));
      const xt = opts.numericX ? (n > (opts.xTickCount || 12) ? pickIdx(n, opts.xTickCount || kx) : xs.map((_, i) => i))
               : isDate(xs) ? monthIdx(xs, kx) : pickIdx(n, kx);
      for (const i of xt) el("text", { x: X(i), y: h - 6, "text-anchor": "middle" }, ax).textContent = (opts.xFmt || String)(xs[i]);
    }
    for (const v of opts.vlines || []) {
      const i = xs.indexOf(v);
      if (i >= 0) el("line", { x1: X(i), x2: X(i), y1: m.t, y2: h - m.b, class: "fold" }, svg);
    }
    if (opts.hline !== undefined && opts.hline !== null)
      el("line", { x1: m.l, x2: w - m.r, y1: Y(opts.hline), y2: Y(opts.hline), class: "fold" }, svg);

    for (const s of shown) {
      if (s.band) {
        let d = "", back = "";
        s.band.hi.forEach((v, i) => { if (v !== null) d += (d ? "L" : "M") + X(i).toFixed(1) + "," + Y(v).toFixed(1); });
        for (let i = n - 1; i >= 0; i--) { const v = s.band.lo[i]; if (v !== null) back += "L" + X(i).toFixed(1) + "," + Y(v).toFixed(1); }
        el("path", { d: d + back + "Z", fill: s.color, opacity: 0.09, stroke: "none" }, svg);
      }
      let d = "", pen = false;
      s.values.forEach((v, i) => {
        if (v === null || !isFinite(v)) { pen = false; return; }
        d += (pen ? "L" : "M") + X(i).toFixed(1) + "," + Y(v).toFixed(1); pen = true;
      });
      el("path", { d, fill: "none", stroke: s.color, "stroke-width": s.width || 1.5, "stroke-dasharray": s.dash,
                   "stroke-linejoin": "round" }, svg);
      if (opts.dots) s.values.forEach((v, i) => { if (v !== null) el("circle", { cx: X(i), cy: Y(v), r: 2.6, fill: s.color }, svg); });
    }

    // crosshair
    const xh = el("line", { y1: m.t, y2: h - m.b, class: "xhair", visibility: "hidden" }, svg);
    const hit = el("rect", { x: m.l, y: m.t, width: w - m.l - m.r, height: h - m.t - m.b, fill: "transparent" }, svg);
    hit.addEventListener("mousemove", ev => {
      const r = svg.getBoundingClientRect();
      const px = (ev.clientX - r.left) * (w / r.width);
      let best = 0, bd = Infinity;
      for (let i = 0; i < n; i++) { const dd = Math.abs(X(i) - px); if (dd < bd) { bd = dd; best = i; } }
      xh.setAttribute("x1", X(best)); xh.setAttribute("x2", X(best)); xh.setAttribute("visibility", "visible");
      const rows = shown.map(s => `<div class="r"><span><i class="sw" style="background:${s.color}"></i>${s.label}</span><span>${s.values[best] === null ? "–" : (opts.tipFmt || opts.yFmt || String)(s.values[best])}</span></div>`).join("");
      showTip(`<div>${(opts.tipTitle || (i => xs[i]))(best)}</div>${rows}`, ev);
    });
    hit.addEventListener("mouseleave", () => { xh.setAttribute("visibility", "hidden"); hideTip(); });
    if (opts.onClick) hit.addEventListener("click", ev => {
      const r = svg.getBoundingClientRect(), px = (ev.clientX - r.left) * (w / r.width);
      let best = 0, bd = Infinity;
      for (let i = 0; i < n; i++) { const dd = Math.abs(X(i) - px); if (dd < bd) { bd = dd; best = i; } }
      opts.onClick(best);
    });
  }

  /* For ISO-date x values: indices where a new month starts, thinned to fit. */
  function monthIdx(xs, k) {
    const idx = [];
    for (let i = 1; i < xs.length; i++) if (String(xs[i]).slice(0, 7) !== String(xs[i - 1]).slice(0, 7)) idx.push(i);
    if (!idx.length) return pickIdx(xs.length, k);
    const step = Math.ceil(idx.length / Math.max(1, k));
    return idx.filter((_, j) => j % step === 0);
  }
  const isDate = xs => xs.length && /^\d{4}-\d{2}-\d{2}$/.test(String(xs[0]));

  function pickIdx(n, k) {
    if (n <= k) return [...Array(n).keys()];
    const out = [];
    for (let j = 0; j < k; j++) out.push(Math.round((j * (n - 1)) / (k - 1)));
    return [...new Set(out)];
  }

  /* bars: one value per x, coloured by sign */
  function bars(host, opts) {
    remember(host, () => bars(host, opts));
    const { svg, w, h } = frame(host);
    const m = { l: 50, r: 8, t: 6, b: 22 };
    const v = opts.values, n = v.length;
    if (!n) return;
    const fin = v.filter(x => x !== null);
    const yt = niceTicks(Math.min(0, ...fin), Math.max(0, ...fin), 4);
    const Y = x => m.t + (h - m.t - m.b) * (1 - (x - yt.lo) / (yt.hi - yt.lo));
    const bw = (w - m.l - m.r) / n;
    const ax = el("g", { class: "ax" }, svg);
    for (const t of yt.ticks) {
      el("line", { x1: m.l, x2: w - m.r, y1: Y(t), y2: Y(t), class: t === 0 ? "zero" : "grid-l" }, svg);
      el("text", { x: m.l - 6, y: Y(t) + 3.5, "text-anchor": "end" }, ax).textContent = (opts.yFmt || String)(t);
    }
    const kx = Math.max(2, Math.floor((w - m.l - m.r) / 80));
    for (const i of isDate(opts.x) ? monthIdx(opts.x, kx) : pickIdx(n, kx))
      el("text", { x: m.l + bw * (i + 0.5), y: h - 6, "text-anchor": "middle" }, ax).textContent = (opts.xFmt || String)(opts.x[i]);
    const g = el("g", {}, svg);
    v.forEach((x, i) => {
      if (x === null) return;
      const y0 = Y(0), y1 = Y(x);
      const r = el("rect", { x: m.l + bw * i + (bw > 3 ? 0.5 : 0), width: Math.max(0.8, bw - (bw > 3 ? 1 : 0)),
                             y: Math.min(y0, y1), height: Math.max(0.5, Math.abs(y1 - y0)),
                             fill: x >= 0 ? "var(--pos)" : "var(--neg)", opacity: 0.85 }, g);
      r.addEventListener("mousemove", ev => showTip(`<div>${opts.x[i]}</div><div>${(opts.tipFmt || opts.yFmt || String)(x)}</div>`, ev));
      r.addEventListener("mouseleave", hideTip);
    });
  }

  /* forest: rows of estimate + interval on one shared axis; optional hollow second marker */
  function forest(host, opts) {
    remember(host, () => forest(host, opts));
    const { svg, w, h } = frame(host);
    const rows = opts.rows;
    if (!rows.length) { el("text", { x: w / 2, y: h / 2, "text-anchor": "middle", class: "lbl" }, svg).textContent = "No data"; return; }
    const lw = opts.labelWidth || 120, m = { l: lw, r: 14, t: 4, b: 20 };
    let lo = 0, hi = 0;
    for (const r of rows) for (const o of [r, r.alt]) if (o) for (const k of ["lo", "hi", "mean"]) if (o[k] !== null && o[k] !== undefined) { lo = Math.min(lo, o[k]); hi = Math.max(hi, o[k]); }
    const xt = niceTicks(lo, hi, Math.max(3, Math.floor((w - lw) / 70)));
    const X = v => m.l + (w - m.l - m.r) * ((v - xt.lo) / (xt.hi - xt.lo));
    const rh = (h - m.t - m.b) / rows.length;
    const ax = el("g", { class: "ax" }, svg);
    for (const t of xt.ticks) {
      el("line", { x1: X(t), x2: X(t), y1: m.t, y2: h - m.b, class: t === 0 ? "zero" : "grid-l" }, svg);
      el("text", { x: X(t), y: h - 6, "text-anchor": "middle" }, ax).textContent = (opts.xFmt || String)(t);
    }
    rows.forEach((r, i) => {
      const cy = m.t + rh * (i + 0.5);
      const g = el("g", { style: opts.onClick ? "cursor:pointer" : null }, svg);
      el("rect", { x: 0, y: cy - rh / 2, width: w, height: rh, fill: "transparent" }, g);
      const t = el("text", { x: 4, y: cy + 4, class: "lbl" }, g);
      t.textContent = r.label;
      if (r.alt && r.alt.mean !== null) {
        el("line", { x1: X(r.alt.lo), x2: X(r.alt.hi), y1: cy + 5, y2: cy + 5, stroke: "var(--ink-3)", "stroke-width": 1 }, g);
        el("circle", { cx: X(r.alt.mean), cy: cy + 5, r: 3, fill: "var(--panel)", stroke: "var(--ink-3)" }, g);
      }
      if (r.mean !== null) {
        el("line", { x1: X(r.lo), x2: X(r.hi), y1: cy - 1, y2: cy - 1, stroke: r.color || "var(--ink)", "stroke-width": 2 }, g);
        el("rect", { x: X(r.mean) - 3.5, y: cy - 4.5, width: 7, height: 7, fill: r.color || "var(--ink)" }, g);
      }
      g.addEventListener("mousemove", ev => showTip(r.tip || `${r.label}: ${(opts.xFmt || String)(r.mean)}`, ev));
      g.addEventListener("mouseleave", hideTip);
      if (opts.onClick) g.addEventListener("click", () => opts.onClick(r));
    });
  }

  /* signed horizontal bars with values written at the end */
  function hbars(host, opts) {
    remember(host, () => hbars(host, opts));
    const { svg, w, h } = frame(host);
    const rows = opts.rows, lw = 76, m = { l: lw, r: 54, t: 4, b: 4 };
    const vals = rows.map(r => r.value || 0);
    const lo = Math.min(0, ...vals), hi = Math.max(0, ...vals);
    const X = v => m.l + (w - m.l - m.r) * ((v - lo) / ((hi - lo) || 1));
    const rh = (h - m.t - m.b) / rows.length;
    el("line", { x1: X(0), x2: X(0), y1: m.t, y2: h - m.b, class: "zero" }, svg);
    rows.forEach((r, i) => {
      const cy = m.t + rh * (i + 0.5), v = r.value || 0, bh = Math.min(18, rh * 0.55);
      el("text", { x: 2, y: cy + 4, class: "lbl" }, svg).textContent = r.label;
      el("rect", { x: Math.min(X(0), X(v)), y: cy - bh / 2, width: Math.max(1, Math.abs(X(v) - X(0))), height: bh,
                   fill: r.color || (v >= 0 ? "var(--pos)" : "var(--neg)"), opacity: 0.85 }, svg);
      const t = el("text", { x: w - 2, y: cy + 4, "text-anchor": "end", class: "lbl-n" }, svg);  // values in their own column
      t.textContent = (opts.fmt || String)(v);
    });
  }

  window.Charts = { line, bars, forest, hbars, hideTip };
})();
