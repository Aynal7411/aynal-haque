# Aynal Haque Portfolio

Django portfolio website for Aynal Haque.

## Project structure

- `aynal_portfolio/` — Django project settings and WSGI/ASGI config
- `core/` — main app with portfolio, blog, skills, and team join features
- `service_my/` — service and contact pages app
- `milon/` — Python virtual environment
- `staticfiles/` — collected static assets
- `db.sqlite3` — local SQLite database
- `requirements.txt` — Python dependencies

## Setup

Use the included virtual environment if available, or create one and install dependencies.

### Use the existing virtual environment

```powershell
Set-Location 'd:\Deployed-projects\aynal-haque'
.\milon\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### If you need to create a new virtualenv

```powershell
Set-Location 'd:\Deployed-projects\aynal-haque'
python -m venv milon
.\milon\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the server

```powershell
Set-Location 'd:\Deployed-projects\aynal-haque'
.\milon\Scripts\Activate.ps1
python manage.py runserver
```

If you do not activate the venv, run:

```powershell
d:\Deployed-projects\aynal-haque\milon\Scripts\python.exe manage.py runserver
```

## Common issue

If you see `ModuleNotFoundError: No module named 'axes'`, make sure you are using the project virtual environment rather than the system Python.

## Git workflow

```powershell
git status
git add .
git commit -m "Describe your changes"
git pull --rebase origin main
git push origin main
```

## Notes

- Do not commit `__pycache__/`, `.pyc`, or local virtual environment artifacts.
- Use the existing `requirements.txt` to keep dependencies consistent.
