@echo off
REM Check if a topic is provided
if "%1"=="" (
    echo Usage: git-help.bat ^<topic^>
    exit /b 1
)

REM Replace spaces with %20 for URL encoding
set topic=%1

REM Open the corresponding HTML file
sidekick "C:\Program Files\Git\mingw64\share\doc\git-doc\git-%topic%.html"
