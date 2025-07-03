@echo off
rmdir /s /q build
rmdir /s /q dist
del injector.spec
pyinstaller --clean --onefile --noconsole injector.py
pause
