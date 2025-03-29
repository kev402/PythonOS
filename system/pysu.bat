@echo off
:: Solicitar permisos administrativos
PowerShell -Command "Start-Process cmd -ArgumentList '/c python C:/PythonOS/main.py' -Verb RunAs"
pause
