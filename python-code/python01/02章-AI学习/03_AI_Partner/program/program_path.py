from pathlib import Path

# プログラムパス
BASE_DIR = Path(__file__).resolve().parent      # program/
PROJECT_DIR = BASE_DIR.parent                   # AI-Partner/
RESOURCE_DIR = PROJECT_DIR / "resources"        # AI-Partner/resources/
SESSION_DIR = BASE_DIR / "session_data"         # program/session_data/