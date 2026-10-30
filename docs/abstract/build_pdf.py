"""Render abstract.md to abstract.pdf (A4) with headless Chrome.

The repo and site links sit at the very top; Figure 1 gets its own last page (the optional 1-page diagram).
Run: python docs/abstract/build_pdf.py
"""
import html
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = "https://mqhnish.github.io/arbpercept/"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def url(u):
    return SITE + u if u.startswith("#") else u


def inline(s):
    """Bold first, then links inside it, so **[x](y).** works."""
    out = []
    for i, bold in enumerate(re.split(r"\*\*(.+?)\*\*", s)):
        seg = []
        for part in re.split(r"(\[[^\]]+\]\([^)\s]+\))", bold):
            m = re.fullmatch(r"\[([^\]]+)\]\(([^)\s]+)\)", part)
            seg.append(f'<a href="{html.escape(url(m.group(2)))}">{fmt(m.group(1))}</a>' if m else fmt(part))
        out.append(f"<strong>{''.join(seg)}</strong>" if i % 2 else "".join(seg))
    return "".join(out)


def fmt(s):
    s = html.escape(s, quote=False)
    s = s.replace("ℓ̄", '<span class="ovl">ℓ</span>')  # Plex puts the combining macron beside the ℓ
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def links_line(s):
    """The repo/site line, as the PDF's header: the website first, then the code."""
    site, repo = (re.search(rf"{p}/\S+", s).group(0) for p in (r"mqhnish\.github\.io", r"github\.com"))
    return (f'<div class="site">Best viewed on our website, with interactive charts: '
            f'<a href="https://{site}/">{site}</a></div>'
            f'<div class="code">Code: <a href="https://{repo}">{repo}</a></div>')


def body(lines):
    out, figure, top, i, seen_h2 = [], "", "", 0, False
    while i < len(lines):
        l = lines[i].strip()
        i += 1
        if not l:
            continue
        if l.startswith("# "):
            out.append(f"<h1>{fmt(l[2:])}</h1>")
        elif l.startswith("## "):
            seen_h2 = True
            out.append(f"<h2>{inline(l[3:])}</h2>")
        elif l.startswith("### "):
            out.append(f"<h3>{inline(l[4:])}</h3>")
        elif not seen_h2:
            top = links_line(l)
        elif l == "[formula]":
            out.append(f'<p class="formula"><img src="{(HERE / "formula.png").as_uri()}" alt="Score formula"></p>')
        elif l == "[architecture diagram]":
            figure = f'<img src="{(HERE / "architecture.png").as_uri()}" alt="Figure 1">'
        elif l.startswith("_") and l.endswith("_"):
            cap = fmt(l[1:-1])
            figure += f"<p class=\"cap\">{re.sub(r'^(Figure \d+\.)', r'<strong>\1</strong>', cap)}</p>"
        elif l.startswith("|"):
            rows = [l]
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows if not re.fullmatch(r"\|[\s:|-]+\|", r)]
            head = "".join(f"<th>{inline(c)}</th>" for c in cells[0])
            rest = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in cells[1:])
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{rest}</tbody></table>")
        elif re.match(r"^[-*]\s+", l):
            items = [l]
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(lines[i].strip())
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(re.sub(r'^[-*]\s+', '', x))}</li>" for x in items) + "</ul>")
        else:
            out.append(f"<p>{inline(l)}</p>")
    return top, "\n".join(out), figure


CSS = """
@page { size: A4; margin: 14mm 16mm 14mm 16mm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font: 9.6pt/1.4 "IBM Plex Sans", "Helvetica Neue", Arial, sans-serif; color: #1a1a1a; }
.top { text-align: center; padding: 0 0 6pt; margin-bottom: 8pt; border-bottom: 1.5pt solid #1155cc; }
.top .site { font-size: 11pt; font-weight: 600; }
.top .code { font-size: 9.6pt; color: #555; margin-top: 1pt; }
.top a { color: #1155cc; text-decoration: none; }
h1 { font: 600 19pt/1.15 "Fraunces", Georgia, serif; margin: 0 0 4pt; }
h2 { font: 600 12.2pt/1.2 "Fraunces", Georgia, serif; margin: 9pt 0 3pt; break-after: avoid; }
h3 { font-size: 10pt; font-weight: 600; margin: 6pt 0 2pt; break-after: avoid; }
p { margin: 0 0 4pt; }
ul { margin: 0 0 4pt; padding-left: 14pt; }
li { margin: 0 0 2pt; }
a { color: #1155cc; text-decoration: underline; text-decoration-thickness: 0.5pt; text-underline-offset: 1.5pt; }
.ovl { text-decoration: overline; text-decoration-thickness: 0.6pt; text-decoration-skip-ink: none; }
code { font-family: "IBM Plex Mono", Menlo, monospace; font-size: 0.92em; }
.formula { text-align: center; margin: 5pt 0 6pt; }
.formula img { width: 92mm; }
table { width: 100%; border-collapse: collapse; margin: 3pt 0 6pt; font-size: 8.9pt; break-inside: avoid; }
th, td { border: 0.6pt solid #c9c6bb; padding: 2.5pt 4.5pt; text-align: left; vertical-align: top; }
th { background: #eef2f8; font-weight: 600; }
@page wide { size: A4 landscape; margin: 12mm 14mm; }
.figure { page: wide; break-before: page; display: flex; flex-direction: column; justify-content: center;
          min-height: 180mm; }
.figure img { width: 100%; }
.cap { text-align: center; font-size: 9pt; color: #555; margin-top: 8pt; }
"""

FONTS = ("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600"
         "&family=IBM+Plex+Mono&family=IBM+Plex+Sans:ital,wght@0,400;0,600;1,400&display=block")


def main():
    top, main_html, figure = body((HERE / "abstract.md").read_text().splitlines())
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Latency-aware cross-venue arbitrage</title>
<link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head><body>
<div class="top">{top}</div>
{main_html}
<div class="figure">{figure}</div>
</body></html>"""
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "abstract.html"
        src.write_text(page)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=15000", f"--print-to-pdf={HERE / 'abstract.pdf'}", src.as_uri()],
                       check=True, capture_output=True)
    print(HERE / "abstract.pdf")


if __name__ == "__main__":
    main()
