#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
"""
Setup script to scaffold data portfolio projects.

Usage:
    python setup_portfolio_projects.py --project global-infectious-disease-surveillance
    python setup_portfolio_projects.py --all
"""

from __future__ import annotations
import argparse
from pathlib import Path
from textwrap import dedent

BASE_DIR = Path(__file__).resolve().parent

PROJECTS = {
    "global-infectious-disease-surveillance": {
        "folders": [
            "data/raw",
            "data/processed",
            "data_ingestion",
            "modeling",
            "nlp_analysis",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn",
            "prophet", "requests", "keybert", "nltk", "geopandas", "pycountry",
            "jupyter", "python-dotenv"
        ],
        "description": "Global infectious disease outbreak analysis & forecasting.",
    },
    "us-flight-delay-prediction": {
        "folders": [
            "data/raw",
            "data/processed",
            "cleaning",
            "feature_engineering",
            "models/saved_models",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn",
            "xgboost", "lightgbm", "requests", "holidays", "jupyter",
            "python-dotenv"
        ],
        "description": "US DOT flight delay prediction with weather & congestion features.",
    },
    "retail-customer-segmentation": {
        "folders": [
            "data/raw",
            "data/processed",
            "rfm",
            "clustering",
            "nlp",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn",
            "umap-learn", "textblob", "jupyter", "python-dotenv"
        ],
        "description": "RFM + clustering segmentation on ecommerce customers.",
    },
    "crypto-anomaly-detection": {
        "folders": [
            "data/raw",
            "data/processed",
            "api",
            "lstm",
            "volatility",
            "sentiment",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn",
            "scikit-learn", "torch", "statsmodels", "arch",
            "requests", "textblob", "jupyter", "python-dotenv"
        ],
        "description": "LSTM + anomaly detection on cryptocurrency time series.",
    },
    "supply-chain-risk-index": {
        "folders": [
            "data/raw",
            "data/processed",
            "trade_api",
            "nlp",
            "risk_model",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn",
            "scikit-learn", "networkx", "requests", "spacy",
            "textblob", "jupyter", "python-dotenv"
        ],
        "description": "Supply chain risk scoring from trade flows + disruption news.",
    },
    "esg-reporting-classifier": {
        "folders": [
            "data/raw_filings",
            "data/processed",
            "sec_scraper",
            "bert_model",
            "topic_modeling",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn",
            "scikit-learn", "torch", "transformers", "datasets",
            "sentencepiece", "bertopic", "umap-learn", "hdbscan",
            "beautifulsoup4", "lxml", "requests", "jupyter",
            "python-dotenv"
        ],
        "description": "BERT-based ESG classifier for SEC filings.",
    },
    "energy-demand-forecasting": {
        "folders": [
            "data/raw",
            "data/processed",
            "eia_api",
            "weather",
            "forecasting",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn",
            "scikit-learn", "prophet", "torch",
            "statsmodels", "requests", "jupyter", "python-dotenv"
        ],
        "description": "Energy load forecasting using EIA + NOAA weather.",
    },
    "restaurant-inspection-prediction": {
        "folders": [
            "data/raw",
            "data/processed",
            "cleaning",
            "classification",
            "menu_scraper",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn",
            "scikit-learn", "geopandas", "shapely",
            "requests", "beautifulsoup4", "lxml",
            "jupyter", "python-dotenv"
        ],
        "description": "Predicting restaurant inspection risk in NYC.",
    },
    "natural-disaster-damage-cv": {
        "folders": [
            "data/raw/before",
            "data/raw/after",
            "data/processed",
            "satellite_data",
            "preprocessing",
            "cnn_model",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn",
            "torch", "torchvision", "rasterio", "opencv-python",
            "albumentations", "geopandas", "shapely",
            "jupyter", "python-dotenv"
        ],
        "description": "CV model on Sentinel-2 imagery for damage classification.",
    },
    "fake-news-detection-transformers": {
        "folders": [
            "data/raw",
            "data/processed",
            "datasets_loader",
            "transformer_model",
            "analysis",
            "notebooks",
            "tableau",
            "utils",
        ],
        "requirements": [
            "pandas", "numpy", "matplotlib", "seaborn",
            "scikit-learn", "torch", "transformers",
            "datasets", "umap-learn", "hdbscan", "nltk",
            "jupyter", "python-dotenv"
        ],
        "description": "Transformer-based fake news detection & reliability analysis.",
    },
}

CONFIG_TEMPLATE = dedent(
    """\
    \"\"\" 
    Central configuration for paths, API keys, and runtime settings.
    Generated for project: {project_name}
    \"\"\" 

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
        \"\"\"Get environment variable with optional default.\"\"\"
        return os.getenv(name, default)


     def require_env(name: str) -> str:
        \"\"\"Get an env var or raise helpful error if missing.\"\"\"
        value = os.getenv(name)
        if not value:
            raise RuntimeError(
                f"Required environment variable '{{name}}' is not set. "
                f"Set it in your shell or in a .env file at {{BASE_DIR}}"
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

    SETTINGS = {{
        "ENV": get_env("ENV", "dev"),
        "MAX_ROWS_DEV": int(get_env("MAX_ROWS_DEV", "50000")),
        "CACHE_DIR": str(BASE_DIR / ".cache"),
        "LOG_LEVEL": get_env("LOG_LEVEL", "INFO"),
    }}

    CACHE_DIR = Path(SETTINGS["CACHE_DIR"])
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    """
)


def create_project(name: str) -> None:
    if name not in PROJECTS:
        raise SystemExit(f"Unknown project '{name}'. Valid: {', '.join(PROJECTS)}")

    meta = PROJECTS[name]
    project_dir = BASE_DIR / name
    project_dir.mkdir(exist_ok=True)

    # Folders
    for f in meta["folders"]:
        (project_dir / f).mkdir(parents=True, exist_ok=True)

    # README
    readme_path = project_dir / "README.md"
    if not readme_path.exists():
        readme_content = dedent(
            f"""\
            # {name}

            {meta['description']}

            ## Quick Start

            ```bash
            pip install -r requirements.txt
            # Add your run commands here
            ```

            """
        )
        readme_path.write_text(readme_content, encoding="utf-8")

    # requirements.txt
    req_path = project_dir / "requirements.txt"
    if not req_path.exists():
        req_text = "\n".join(sorted(set(meta["requirements"]))) + "\n"
        req_path.write_text(req_text, encoding="utf-8")

    # config.py
    config_path = project_dir / "config.py"
    if not config_path.exists():
        config_path.write_text(CONFIG_TEMPLATE.format(project_name=name), encoding="utf-8")

    # starter notebooks
    nb1 = project_dir / "notebooks" / "01_eda.ipynb"
    nb2 = project_dir / "notebooks" / "02_modeling.ipynb"
    if not nb1.exists():
        # minimal empty notebooks; you can overwrite later
        empty_nb = {
            "cells": [],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 5,
        }
        import json

        nb1.write_text(json.dumps(empty_nb, indent=2), encoding="utf-8")
        nb2.write_text(json.dumps(empty_nb, indent=2), encoding="utf-8")

    print(f"✔ Created/updated scaffold for {name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project",
        help="Name of project to set up (see PROJECTS dict).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Create all projects defined in this script.",
    )
    args = parser.parse_args()

    if args.all:
        for name in PROJECTS:
            create_project(name)
    elif args.project:
        create_project(args.project)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


# In[ ]:




