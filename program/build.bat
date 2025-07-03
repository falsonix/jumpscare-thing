@echo off
rmdir /s /q build
rmdir /s /q dist
del thebiteof87.spec
pyinstaller --clean --onefile --noconsole ^
    --icon=myicon.ico ^
    --add-data "ffplay.exe;." ^
    --add-data "jumpscare.mp4;." ^
    --add-data "jumpscare_config.json;." ^
    thebiteof87.py
pause
