$videosPath = Join-Path -Path $HOME -ChildPath "Videos"
$fileExtension = "*.mkv"

$latestMkvFile = Get-ChildItem -Path $videosPath -Filter $fileExtension -File |
                 Sort-Object -Property LastWriteTime -Descending |
                 Select-Object -First 1

if ($null -eq $latestMkvFile) {
    Write-Error "No .mkv files found in $videosPath"
    exit 1
}

$outputFilePath = Join-Path -Path $videosPath -ChildPath ([System.IO.Path]::ChangeExtension($latestMkvFile.Name, "mp4"))

Write-Host "Found latest MKV: $($latestMkvFile.FullName)"
Write-Host "Converting to MP4: $outputFilePath"

try {
    & ffmpeg -i $latestMkvFile.FullName -codec copy $outputFilePath

    if ($LASTEXITCODE -eq 0 -and (Test-Path -Path $outputFilePath)) {
        Write-Host "Conversion completed successfully!" -ForegroundColor Green
    } else {
        Write-Error "Conversion failed with exit code: $LASTEXITCODE"
    }
}
catch {
    Write-Error "An error occurred during conversion: $_"
    exit 1
}

