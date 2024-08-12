@echo off
if "%1"=="" (
    echo Usage: git-help.bat ^<topic^>
    exit /b 1
)
set topic=%1
sidekick "C:\Program Files\Git\mingw64\share\doc\git-doc\git-%topic%.html"
