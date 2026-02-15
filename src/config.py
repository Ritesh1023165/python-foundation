from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT/"data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
INPUT_DATA_DIR = DATA_DIR/"input"
INPUT_DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DATA_DIR = DATA_DIR/"output"
OUTPUT_DATA_DIR.mkdir(parents=True, exist_ok=True)