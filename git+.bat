@echo off
if "%1" == "switch" (
    if "%2" == "" (
        echo No branch is specified to switch to.
    ) else (
        git branch --set-upstream-to=origin/%2 %2
        git switch %2
        git pull %2
    )
) else if "%1" == "push" (
    if "%2" == "" (
        echo No branch is specified to push to remote.
    ) else (
        git push --set-upstream origin %2
    )
) else if "%1" == "reset" (
    git clean -fd
    git reset HEAD~ --hard
    git pull
) else if "%1" == "amend" (
    git commit --amend --no-edit --allow-empty
) else (
    echo "git+.bat [switch/push/reset/amend] [<branch>]"
)
