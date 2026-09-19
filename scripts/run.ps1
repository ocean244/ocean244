# Skrypt orkiestracyjny ocean244
$ErrorActionPreference = "Stop"

Write-Host "=== [ocean244] Uruchamianie srodowiska produkcyjnego ===" -ForegroundColor Cyan
Write-Host "Lokalizacja: $(Get-Location)" -ForegroundColor Gray

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCmd) {
    Write-Host "[+] Wykryto interpreter Python: $($pythonCmd.Source)" -ForegroundColor Green
    python -m src.main
} else {
    Write-Host "[!] Brak binarnego interpretera Python w PATH." -ForegroundColor Yellow
}

$gitStatus = git status --porcelain
if ($gitStatus) {
    Write-Host "[!] Wykryto zmiany do zatwierdzenia." -ForegroundColor Yellow
} else {
    Write-Host "[+] Repozytorium zsynchronizowane i czyste." -ForegroundColor Green
}

Write-Host "=== [ocean244] Egzekucja zakonczona sukcesem ===" -ForegroundColor Green
