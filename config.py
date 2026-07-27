import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Directories
UPLOADS_DIR = BASE_DIR / "uploads"
REPORTS_DIR = BASE_DIR / "reports"
MODELS_DIR = BASE_DIR / "models"
ASSETS_DIR = BASE_DIR / "assets"

# Ensure directories exist
for directory in [UPLOADS_DIR, REPORTS_DIR, MODELS_DIR, ASSETS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

APP_NAME = "InsightAI Studio"
