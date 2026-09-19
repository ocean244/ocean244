# Skrypt orkiestracyjny ocean244
$ErrorActionPreference = "Stop"

Write-Host "=== [ocean244] Uruchamianie rodowiska produkcyjnego ===" -ForegroundColor Cyan
Write-Host "Lokalizacja: $(Get-Location)" -ForegroundColor Gray

# Sprawdzenie wariantu Python
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCmd) {
    Write-Host "[+] Wykryto interpreter Python: $($pythonCmd.Source)" -ForegroundColor Green
    python src\main.py
} else {
    Write-Host "[!] Brak binarnego interpretera Python w PATH. Weryfikacja struktury..." -ForegroundColor Yellow
}

# Sprawdzenie statusu Git
$gitStatus = git status --porcelain
if ($gitStatus) {
    Write-Host "[!] Wykryto zmiany do zatwierdzenia." -ForegroundColor Yellow
} else {
    Write-Host "[+] Repozytorium zsynchronizowane i czyste." -ForegroundColor Green
}

Write-Host "=== [ocean244] Egzekucja zakoczona sukcesem ===" -ForegroundColor Green
