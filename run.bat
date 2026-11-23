@echo off
REM Starts the e-portfolio locally at http://127.0.0.1:8000/
REM Creates the virtual environment and installs Django the first time.
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
    echo Creating virtual environment...
    py -3.12 -m venv venv 2>nul || py -m venv venv || python -m venv venv
    if errorlevel 1 (
        echo Could not create the virtual environment. Is Python installed?
        pause
        exit /b 1
    )
)

"venv\Scripts\python.exe" -c "import django" 2>nul
if errorlevel 1 (
    echo Installing dependencies...
    "venv\Scripts\python.exe" -m pip install -r requirements.txt
)

start "" "http://127.0.0.1:8000/"
"venv\Scripts\python.exe" manage.py runserver 127.0.0.1:8000
pause
