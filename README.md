# TaskManager

Backend API for TaskManager, built with Python 3.12, FastAPI, and Uvicorn.

## Setup

Create and activate a Python 3.12 virtual environment, then install the
dependencies:

```bash
python -m venv .venv
```

On Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

From the repository root:

```bash
uvicorn app.main:app --reload
```
## Funzionalità in sviluppo

- Issue #15: aggiungere un livello di priorità ai task (alta, media, bassa).
