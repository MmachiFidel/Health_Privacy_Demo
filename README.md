# Fidelia Ivoke — Sanitized Sample Code
This repository contains **sanitized example code** demonstrating key components from my health-data engineering work:

- A small FastAPI app (`app/main.py`) showing privacy-aware endpoints
- A pseudonymization utility (`privacy/pseudonymize.py`)
- A simple differential-privacy helper (`dp/mechanisms.py`)
- Minimal SQLAlchemy models (`db/models.py`)

**Purpose:** shareable portfolio material for academic application — no proprietary data or sensitive details included.

## How to run
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Notes
- All data handling is **sanitized** and uses fabricated/example data only.
- This is a demonstration scaffold you can extend for real projects.
