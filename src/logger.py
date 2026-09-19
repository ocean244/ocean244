import logging
import sys
from src.config import config

def setup_logger():
    logger = logging.getLogger(config.APP_NAME)
    logger.setLevel(config.LOG_LEVEL)
    
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(console_handler)
        
    return logger

logger = setup_logger()
