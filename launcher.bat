@echo off

cd virtualenv\Scripts
call activate.bat
cd ..\..
call python main.py
pause
