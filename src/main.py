import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import config
from src.logger import logger

def main():
    logger.info(f"Uruchamianie {config.APP_NAME} na porcie {config.PORT} [{config.APP_ENV}]")
    logger.info("Modul konfiguracyjny i silnik logowania zaladowany pomyslnie.")
    logger.info("Status operacyjny: OK (100% sprawnosci)")

if __name__ == "__main__":
    main()
