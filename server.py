"""
Gestural local server.

Run:  python3 server.py   then open http://localhost:8000

What it does:
  1. Serves the files in this folder (index.html etc.). The browser only allows
     webcam access on http://localhost, not when opening the file directly.
  2. /api/search?q=rain   -> asks Freesound for sounds, adding the secret API key
                             from .env (so the key never reaches the browser).
  3. /api/audio?url=...   -> downloads a Freesound preview mp3 and passes it on
                             (avoids the browser's CORS blocking).

Only the Python standard library is used.
"""

import json
import logging
import os
import ssl
import urllib.error
import urllib.parse
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000
HERE = os.path.dirname(os.path.abspath(__file__))
FREESOUND_SEARCH_URL = "https://freesound.org/apiv2/search/text/"
ALLOWED_AUDIO_HOSTS = ("freesound.org",)  # also allows subdomains like cdn.freesound.org

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("gestural")


def load_env(path):
    """Read KEY=value lines from a .env file into a dict (tiny, no library needed)."""
    values = {}
    if not os.path.exists(path):
        return values
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


ENV = load_env(os.path.join(HERE, ".env"))
API_KEY = ENV.get("FREESOUND_API_KEY") or os.environ.get("FREESOUND_API_KEY", "")
if API_KEY in ("", "your_key_here"):
    API_KEY = ""


def fetch(url, timeout=15):
    """Download a URL and return (bytes, content_type)."""
    req = urllib.request.Request(url, headers={"User-Agent": "Gestural-class-project/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read(), resp.headers.get("Content-Type", "application/octet-stream")


def host_allowed(url):
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    return any(host == h or host.endswith("." + h) for h in ALLOWED_AUDIO_HOSTS)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HERE, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if parsed.path == "/api/search":
            return self.handle_search(params.get("q", [""])[0].strip())
        if parsed.path == "/api/audio":
            return self.handle_audio(params.get("url", [""])[0])
        if parsed.path.startswith("/.env"):
            return self.send_json(404, {"error": "not found"})  # never serve secrets
        return super().do_GET()

    # ---- API: search Freesound ----
    def handle_search(self, query):
        if not API_KEY:
            log.warning("Search requested but no FREESOUND_API_KEY in .env")
            return self.send_json(503, {"error": "no_key",
                                        "message": "No Freesound API key yet. See README: 'Setting up Freesound search'."})
        if not query:
            return self.send_json(400, {"error": "empty", "message": "Type something to search."})
        url = FREESOUND_SEARCH_URL + "?" + urllib.parse.urlencode({
            "query": query,
            "fields": "id,name,username,license,duration,previews",
            "filter": "duration:[0.5 TO 60]",
            "page_size": 12,
            "token": API_KEY,
        })
        log.info("Freesound search: %r", query)
        try:
            body, _ = fetch(url)
            data = json.loads(body)
        except urllib.error.HTTPError as e:
            log.error("Freesound search failed: HTTP %s (check your API key)", e.code)
            return self.send_json(502, {"error": "freesound", "message": f"Freesound said HTTP {e.code}. Is the API key correct?"})
        except Exception as e:  # network, SSL, JSON...
            log.error("Freesound search error: %s", self.explain(e))
            return self.send_json(502, {"error": "network", "message": self.explain(e)})

        results = [{
            "id": r.get("id"),
            "name": r.get("name"),
            "username": r.get("username"),
            "license": r.get("license"),
            "duration": r.get("duration"),
            "preview": (r.get("previews") or {}).get("preview-hq-mp3"),
            "page": f"https://freesound.org/s/{r.get('id')}/",
        } for r in data.get("results", [])]
        log.info("  -> %d results", len(results))
        self.send_json(200, {"results": results})

    # ---- API: proxy an audio preview ----
    def handle_audio(self, url):
        if not url.startswith("https://") or not host_allowed(url):
            log.warning("Blocked audio URL (not freesound.org): %s", url)
            return self.send_json(400, {"error": "bad_url"})
        try:
            body, ctype = fetch(url, timeout=30)
        except Exception as e:
            log.error("Audio download failed: %s", self.explain(e))
            return self.send_json(502, {"error": "download", "message": self.explain(e)})
        log.info("Audio loaded: %s (%d KB)", url.rsplit("/", 1)[-1], len(body) // 1024)
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # ---- helpers ----
    @staticmethod
    def explain(e):
        if isinstance(e, urllib.error.URLError) and isinstance(e.reason, ssl.SSLError):
            return ("SSL certificate problem. On macOS with python.org Python, run "
                    "'Install Certificates.command' from your Python folder in Applications.")
        return str(e)

    def send_json(self, status, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Quieter default logs: skip successful static file requests, keep errors.
        if len(args) > 1 and str(args[1]).startswith(("2", "3")) and "/api/" not in str(args[0]):
            return
        log.info("%s - %s", self.address_string(), fmt % args)


def main():
    log.info("Gestural server starting on http://localhost:%d", PORT)
    log.info("Freesound search: %s", "ENABLED (key found in .env)" if API_KEY else "DISABLED (no key in .env yet — built-in sound still works)")
    server = ThreadingHTTPServer(("localhost", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        log.info("Shutting down. Bye!")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
