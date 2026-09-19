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
from src.router import APIRouter

class CoreHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        status_code, response_data = APIRouter.handle_request(self.path)
        
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(response_data, indent=2).encode("utf-8"))

    def log_message(self, format, *args):
        logger.info(f"HTTP {self.command} {self.path} - {self.address_string()} - {format % args}")

def run_server():
    handler = CoreHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", config.PORT), handler) as httpd:
        logger.info(f"Serwer HTTP uruchomiony na porcie {config.PORT} [http://localhost:{config.PORT}/health]")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("Zatrzymywanie serwera HTTP...")
            httpd.server_close()

if __name__ == "__main__":
    run_server()
