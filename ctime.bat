@echo off
powershell -Command "$result = Measure-Command { %* 2>&1 | Tee-Object -Variable output }; $output; $result.TotalSeconds"
