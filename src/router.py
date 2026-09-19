import json
import time

START_TIME = time.time()

class APIRouter:
    @staticmethod
    def handle_request(path: str) -> tuple[int, dict]:
        if path in ["/health", "/"]:
            return 200, {
                "status": "OK",
                "service": "ocean244_core",
                "code": 200
            }
        elif path == "/api/v1/status":
            return 200, {
                "status": "ACTIVE",
                "uptime_seconds": round(time.time() - START_TIME, 2),
                "engine": "Python 3.12",
                "readiness": "100%"
            }
        else:
            return 404, {
                "error": "Not Found",
                "path": path,
                "code": 404
            }
