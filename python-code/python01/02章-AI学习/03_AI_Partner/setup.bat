@echo off
cd /d %~dp0

echo [1/3] Checking virtual environment...
if not exist .venv (
    py -m venv .venv
)

echo [2/3] Activating virtual environment...
call .venv\Scripts\activate

echo [3/3] Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Setup finished.
pause