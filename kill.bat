@echo off
if "%1"=="" (
    echo Usage: kill.bat ^<process^>
    exit /b 1
)
taskkill /f /im %1.exe