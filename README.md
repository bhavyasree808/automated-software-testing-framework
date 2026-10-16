# Automated Software Testing and Quality Assurance Framework

A portfolio project demonstrating API test automation with Python, pytest, reusable fixtures, positive and negative test cases, and GitHub Actions CI.

## Features
- Health endpoint test
- User API tests for list, read, create, and delete
- Positive and negative validation tests
- Reusable pytest fixture
- CI workflow that runs tests on pushes and pull requests

## Tech stack
Python, Flask, pytest, GitHub Actions.

## Run locally (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v
```

Expected result: **9 tests passed**.

## Run the demo API (optional)

```powershell
python -c "from app.api import create_app; create_app().run(debug=True)"
```

Open `http://127.0.0.1:5000/health`. Stop with `Ctrl+C`.

## Project structure
- `app/api.py` — sample API
- `tests/` — automated test cases and reusable fixture
- `.github/workflows/tests.yml` — GitHub Actions workflow

## Scope and limitations
This is a demo app for learning and portfolio use. Data is stored in memory and resets when the app is recreated. It does not include authentication, production deployment, load testing, or a live third-party API.

## Future improvements
- Add coverage reporting
- Add parameterized tests and schema validation
- Test a separately deployed API using configurable base URLs
- Add API contract and performance tests
