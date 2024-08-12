@echo off
if "%1"=="" (
    echo Usage: git+.bat [squash/merge]
    echo squash: Rebases onto main with interactive rebase
    echo merge: Merges onto main
    exit /b 1
)
if "%1"=="squash" (
    git rebase -i main
)
if "%1"=="merge" AND NOT "%2"=="" (
    git checkout main
    git merge "%2"
)