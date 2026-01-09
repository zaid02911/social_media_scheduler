import logging
import os
from pathlib import Path

PLATFORMS = [
    "Twitter", "Facebook", "LinkedIn", "Instagram"
]

BASE_DIR = Path(__file__).resolve().parent

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = BASE_DIR / "logs" / "app.log"

DATABASE_PATH = "data/database.sqlite"
