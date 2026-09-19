import http.server
import socketserver
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import config
from src.logger import logger

class CoreHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health" or self.path == "/":
            response = {
                "status": "OK",
                "app_name": config.APP_NAME,
                "environment": config.APP_ENV,
                "port": config.PORT
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        logger.info(f"HTTP Request: {self.address_string()} - {format % args}")

def run_server():
    handler = CoreHTTPRequestHandler
    with socketserver.TCPServer(("", config.PORT), handler) as httpd:
        logger.info(f"Serwer HTTP uruchomiony na porcie {config.PORT} [http://localhost:{config.PORT}/health]")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("Zatrzymywanie serwera HTTP...")
            httpd.server_close()

if __name__ == "__main__":
    run_server()
