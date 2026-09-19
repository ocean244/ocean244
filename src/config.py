import os
from pathlib import Path

class Config:
    def __init__(self):
        self.root_dir = Path(__file__).resolve().parent.parent
        self.env_path = self.root_dir / ".env"
        
        if self.env_path.exists():
            with open(self.env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ[k.strip()] = v.strip()
        
        self.APP_NAME = os.getenv("APP_NAME", "ocean244_core")
        self.APP_ENV = os.getenv("APP_ENV", "production")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        self.PORT = int(os.getenv("PORT", "8090"))

config = Config()
