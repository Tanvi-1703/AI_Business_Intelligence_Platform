import os

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
UPLOAD_FOLDER = os.path.join(DATA_FOLDER, "uploads")
RAW_FOLDER = os.path.join(DATA_FOLDER, "raw")
CLEAN_FOLDER = os.path.join(DATA_FOLDER, "cleaned")

DATABASE_FOLDER = os.path.join(BASE_DIR, "database")

REPORT_FOLDER = os.path.join(BASE_DIR, "reports")
PDF_FOLDER = os.path.join(REPORT_FOLDER, "pdf")
IMAGE_FOLDER = os.path.join(REPORT_FOLDER, "images")
EXCEL_FOLDER = os.path.join(REPORT_FOLDER, "excel")

POWERBI_FOLDER = os.path.join(BASE_DIR, "powerbi")

# -----------------------------
# Database
# -----------------------------

DATABASE_NAME = "business.db"

DATABASE_PATH = os.path.join(
    DATABASE_FOLDER,
    DATABASE_NAME
)

# -----------------------------
# Supported Files
# -----------------------------

SUPPORTED_FILES = [
    ".csv",
    ".xlsx"
]