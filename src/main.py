import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import config
from src.logger import logger
from src.server import run_server

def main():
    logger.info(f"Inicjalizacja {config.APP_NAME} [{config.APP_ENV}]...")
    logger.info("Gotowo operacyjna 100%. Uruchamianie usygi...")
    run_server()

if __name__ == "__main__":
    main()
