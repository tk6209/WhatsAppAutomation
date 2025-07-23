# setup.ps1

Write-Host "🛠️ Iniciando ambiente do WhatsAppAutomation..." -ForegroundColor Cyan

# 1. Criar ambiente virtual
if (-Not (Test-Path "venv")) {
    Write-Host "📦 Criando ambiente virtual..." -ForegroundColor Yellow
    python -m venv venv
} else {
    Write-Host "✅ Ambiente virtual já existe."
}

# 2. Ativar ambiente virtual
Write-Host "⚙️ Ativando ambiente virtual..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# 3. Instalar dependências
if (Test-Path "requirements.txt") {
    Write-Host "📚 Instalando dependências do requirements.txt..." -ForegroundColor Yellow
    pip install -r requirements.txt
} else {
    Write-Host "❌ Arquivo requirements.txt não encontrado!" -ForegroundColor Red
    exit
}

# 4. Criar pastas necessárias
if (-Not (Test-Path "logs")) {
    New-Item -ItemType Directory -Path "logs"
    Write-Host "📁 Pasta 'logs' criada."
}
if (-Not (Test-Path "data")) {
    New-Item -ItemType Directory -Path "data"
    Write-Host "📁 Pasta 'data' criada."
}

# 5. Rodar o script principal
if (Test-Path "src\whatsapp_sender.py") {
    Write-Host "`n▶️ Executando whatsapp_sender.py..." -ForegroundColor Green
    python src/whatsapp_sender.py
} else {
    Write-Host "❌ Script src\whatsapp_sender.py não encontrado." -ForegroundColor Red
}
