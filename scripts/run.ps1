# Skrypt uruchomieniowy ocean244
$ErrorActionPreference = "Stop"

Write-Host "=== [ocean244] Inicjalizacja rodowiska ===" -ForegroundColor Cyan
Write-Host "Katalog roboczy: $(Get-Location)" -ForegroundColor Gray

# Sprawdzenie stanu Git
$gitStatus = git status --porcelain
if ($gitStatus) {
    Write-Host "[!] Wykryto niezatwierdzone zmiany w repozytorium." -ForegroundColor Yellow
} else {
    Write-Host "[+] Repozytorium jest czyste." -ForegroundColor Green
}

Write-Host "=== [ocean244] Peny status gotowy do egzekucji ===" -ForegroundColor Green
