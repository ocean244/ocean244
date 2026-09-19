import os
import sys

def main():
    app_name = os.getenv("APP_NAME", "ocean244_core")
    app_env = os.getenv("APP_ENV", "development")
    
    print(f"[SYSTEM] Uruchamianie {app_name} w trybie [{app_env}]...")
    print("[SYSTEM] Status operacyjny: OK (100% sprawnoci)")

if __name__ == "__main__":
    main()
