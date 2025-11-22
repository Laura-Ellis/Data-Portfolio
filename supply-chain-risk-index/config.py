""" 
Central configuration for paths, API keys, and runtime settings.
Generated for project: supply-chain-risk-index
""" 

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv is optional
    pass

BASE_DIR: Path = Path(__file__).resolve().parent

DATA_DIR: Path = BASE_DIR / "data"
RAW_DATA_DIR: Path = DATA_DIR / "raw"
PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"

NOTEBOOKS_DIR: Path = BASE_DIR / "notebooks"
TABLEAU_DIR: Path = BASE_DIR / "tableau"
MODELS_DIR: Path = BASE_DIR / "models"
LOGS_DIR: Path = BASE_DIR / "logs"
SRC_DIR: Path = BASE_DIR / "src"  # optional generic source folder

for _p in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR,
           NOTEBOOKS_DIR, TABLEAU_DIR, MODELS_DIR, LOGS_DIR]:
    _p.mkdir(parents=True, exist_ok=True)


def get_env(name: str, default: str | None = None) -> str | None:
    """Get environment variable with optional default."""
    return os.getenv(name, default)


 def require_env(name: str) -> str:
    """Get an env var or raise helpful error if missing."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Required environment variable '{name}' is not set. "
            f"Set it in your shell or in a .env file at {BASE_DIR}"
        )
    return value


# Common API keys (only use what you need in this project)
WHO_API_KEY = get_env("WHO_API_KEY")
DOT_API_KEY = get_env("DOT_API_KEY")
NOAA_API_KEY = get_env("NOAA_API_KEY")
EIA_API_KEY = get_env("EIA_API_KEY")
NEWS_API_KEY = get_env("NEWS_API_KEY")
UN_COMTRADE_API_KEY = get_env("UN_COMTRADE_API_KEY")
SEC_EDGAR_API_KEY = get_env("SEC_EDGAR_API_KEY")
FEMA_API_KEY = get_env("FEMA_API_KEY")
COINGECKO_API_KEY = get_env("COINGECKO_API_KEY")

ASANA_PAT = get_env("ASANA_PAT")
GITHUB_TOKEN = get_env("GITHUB_TOKEN")

SETTINGS = {
    "ENV": get_env("ENV", "dev"),
    "MAX_ROWS_DEV": int(get_env("MAX_ROWS_DEV", "50000")),
    "CACHE_DIR": str(BASE_DIR / ".cache"),
    "LOG_LEVEL": get_env("LOG_LEVEL", "INFO"),
}

CACHE_DIR = Path(SETTINGS["CACHE_DIR"])
CACHE_DIR.mkdir(parents=True, exist_ok=True)
