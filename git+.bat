@echo off
if "%1" == "squash" (
    if "%2" == "abort" (
        git rebase --abort
    ) else (
        git rebase -i main
    )
) else if "%1" == "merge" (
    if "%2" == "" (
        echo No branch is specified to merge.
    ) else (
        git checkout main
        git merge %2
    )
) else if "%1" == "switch" (
    if "%2" == "" (
        echo No branch is specified to switch to.
    ) else (
        git branch --set-upstream-to=origin/%2 %2
        git switch %2
        git pull %2
    )
) else (
    echo "git+.bat [squash/merge/switch] [abort/<branch>]"
)
