# Skrypt testujcy REST API ocean244
$ErrorActionPreference = "Stop"
$port = 8090
$baseUrl = "http://localhost:$port"

Write-Host "=== [ocean244] Test Weryfikacyjny API / Healthcheck ===" -ForegroundColor Cyan

try {
    Write-Host "[+] Weryfikacja endpointu /health..." -ForegroundColor Gray
    $health = Invoke-RestMethod -Uri "$baseUrl/health" -Method Get -TimeoutSec 5
    Write-Host "[+] Odpowied statusu: $($health.status) | App: $($health.app_name) | Port: $($health.port)" -ForegroundColor Green

    Write-Host "[+] Weryfikacja endpointu /api/v1/status..." -ForegroundColor Gray
    $status = Invoke-RestMethod -Uri "$baseUrl/api/v1/status" -Method Get -TimeoutSec 5
    Write-Host "[+] Odpowied API: OK (Uptime: $($status.uptime_seconds)s)" -ForegroundColor Green

    Write-Host "=== [ocean244] Wszystkie testy API zakoczone sukcesem [100%] ===" -ForegroundColor Green
} catch {
    Write-Host "[!] Bd poczenia z serwerem HTTP na porcie $port. Upewnij si, e 'python -m src.main' jest uruchomiony." -ForegroundColor Red
    Write-Host "[!] Szczegóy bdu: $_" -ForegroundColor Red
    exit 1
}
