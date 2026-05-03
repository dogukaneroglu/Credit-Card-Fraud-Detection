"""Proje kökü ve veri dosyası yolları (tek kaynak)."""

from pathlib import Path

# src/fraud_detection/paths.py -> repo kökü iki üst dizin
_REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = _REPO_ROOT / "data"
DEFAULT_DATA_PATH = DATA_DIR / "creditcard.csv"
