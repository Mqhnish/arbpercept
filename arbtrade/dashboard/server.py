"""The dashboard's web server: static files plus a small JSON API. Standard library only.

    .venv/bin/python -m arbtrade.dashboard [--port 8050] [--open]

It listens on 127.0.0.1 only. Results come from data/reports/ (committed, so they work on any
checkout); the paper trader needs the live extras (websockets, certifi) for live feeds, or our
recordings in data/raw/ for a replay.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import threading
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from arbdata.config import load_config

from . import data as D
from .paper import PaperSession

STATIC = Path(__file__).resolve().parent / "static"
# Set explicitly: on Windows, mimetypes reads the registry, which can map .js to text/plain.
TYPES = {".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8",
         ".js": "text/javascript; charset=utf-8", ".svg": "image/svg+xml"}


class App:
    def __init__(self, reports: Path, paper: PaperSession | None):
        self.reports, self.paper = reports, paper

    def get(self, path: str, q: dict) -> object:
        one = lambda k, default=None: q.get(k, [default])[0]
        if path == "/api/runs":
            return D.list_runs(self.reports)
        if path == "/api/run":
            return D.run_summary(self.reports, one("name"), float(one("fee")), float(one("tau")), one("mode", "optimistic"),
                                 one("cap", "capped"))
        if path == "/api/coins":
            return D.coins(self.reports, one("tag", "_v7_real"), one("mode", "optimistic"), one("cap", "capped"))
        if path == "/api/decay":
            return D.decay(self.reports)
        if path == "/api/notes":
            return D.notes(self.reports)
        if path == "/api/note":
            return {"path": one("path"), "text": D.read_note(self.reports, one("path"))}
        if path == "/api/paper":
            return self.paper.snapshot() if self.paper else {"status": "unavailable"}
        raise KeyError(path)

    def post(self, path: str, body: dict) -> object:
        if self.paper is None:
            raise RuntimeError("the paper trader is not available here")
        if path == "/api/paper/start":
            return self.paper.start(body)
        if path == "/api/paper/stop":
            self.paper.stop()
            return {"ok": True}
        raise KeyError(path)


def make_handler(app: App):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):  # quiet: the page polls every second
            pass

        def _send(self, status: int, body: bytes, ctype: str) -> None:
            self.send_response(status)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, status: int, obj: object) -> None:
            self._send(status, json.dumps(obj, allow_nan=False).encode(), "application/json")

        def _api(self, fn) -> None:
            try:
                self._json(HTTPStatus.OK, fn())
            except KeyError as e:
                self._json(HTTPStatus.NOT_FOUND, {"error": f"not found: {e}"})
            except (ValueError, TypeError, RuntimeError) as e:
                self._json(HTTPStatus.BAD_REQUEST, {"error": str(e)})

        def do_GET(self):
            u = urlparse(self.path)
            if u.path.startswith("/api/"):
                return self._api(lambda: app.get(u.path, parse_qs(u.query)))
            rel = "index.html" if u.path in ("/", "") else u.path.lstrip("/").removeprefix("static/")
            f = (STATIC / rel).resolve()
            if STATIC not in f.parents or not f.is_file():
                return self._send(HTTPStatus.NOT_FOUND, b"not found", "text/plain")
            ctype = TYPES.get(f.suffix) or mimetypes.guess_type(f.name)[0] or "application/octet-stream"
            self._send(HTTPStatus.OK, f.read_bytes(), ctype)

        def do_POST(self):
            u = urlparse(self.path)
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(n) or b"{}") if n else {}
            self._api(lambda: app.post(u.path, body))

    return Handler


def serve(port: int = 8050, open_browser: bool = False) -> None:
    cfg = load_config()
    app = App(cfg.reports_dir, PaperSession(cfg, cfg.reports_dir / "live"))
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(app))
    url = f"http://127.0.0.1:{port}/"
    print(f"arbpercept dashboard on {url} (Ctrl+C to stop)", flush=True)
    if open_browser:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        app.paper.stop()
        httpd.server_close()


def main() -> None:
    ap = argparse.ArgumentParser(description="arbpercept dashboard")
    ap.add_argument("--port", type=int, default=8050)
    ap.add_argument("--open", action="store_true", help="open it in the default browser")
    args = ap.parse_args()
    serve(args.port, args.open)
