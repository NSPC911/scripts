Write-Host "You have two options."
Write-Host "Option A: Activate the virtual environment to use " -NoNewLine
Write-Host "python -m pip" -ForegroundColor Cyan
Write-Host "Option B: Use " -NoNewLine
Write-Host "uv pip install" -ForegroundColor Cyan -NoNewLine
Write-Host " for temporary installations."
Write-Host "          That means you still either need to use " -NoNewLine
Write-Host "uv run <script>" -ForegroundColor Cyan -NoNewLine
Write-Host " or activate the virtual environment." -BackgroundColor Black
Write-Host ""
Write-Host "The choice is yours."
