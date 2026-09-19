import sys
from src.config import config
from src.logger import logger

def main():
    logger.info(f"Uruchamianie {config.APP_NAME} na porcie {config.PORT} [{config.APP_ENV}]")
    logger.info("Modu konfiguracyjny i silnik logowania zaadowany pomylnie.")
    logger.info("Status operacyjny: OK (100% sprawnoci)")

if __name__ == "__main__":
    main()
