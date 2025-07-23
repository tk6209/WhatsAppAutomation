# 📲 WhatsAppAutomation

Automação de envio de mensagens via WhatsApp — estrutura reorganizada com boas práticas em Python.

## 🚀 Objetivo

Construir uma base robusta e modular para automações com WhatsApp, com foco em legibilidade, escalabilidade e integração futura com bibliotecas como `selenium`, `pyautogui` e `pywhatkit`.

---

## ♻️ Histórico de scripts originais

Este projeto foi reestruturado preservando todos os arquivos anteriores. Os scripts originais estão organizados na pasta:

📁 legacy/
├── NewWhatsapp.py
├── WhatsApp.py
├── WhatsApp2.py
├── WhatsApp3.py
└── WhatsTest.py

yaml
Copiar
Editar

Esses arquivos representam tentativas iniciais e protótipos. Permanecem versionados, mas fora do fluxo principal de execução.

---

## 📁 Estrutura atual

WhatsAppAutomation/
├── src/
│ ├── main.py # Script principal (execução padrão)
│ ├── init.py
│ ├── experiments/ # Protótipos novos ou isolados
│ └── test/ # Testes unitários ou de integração
│
├── legacy/ # Scripts originais preservados
├── logs/ # Logs de execução
├── docs/ # Documentação futura
├── requirements.txt # Dependências do projeto
├── .gitignore # Exclusões do Git
└── README.md # Este documento

yaml
Copiar
Editar

---

## 🧪 Como executar o script principal

```bash
python src/main.py
🔒 Logs
Os logs são gerados automaticamente em:

bash
Copiar
Editar
logs/whatsapp_automation.log
📌 Requisitos (opcionais para automação avançada)
Python 3.9+

selenium, pyautogui, pandas, pywhatkit (ver requirements.txt)

Projeto reestruturado por Vinicius Teixeira

yaml
Copiar
Editar

---

### ✅ Para aplicar:

1. Substitua o conteúdo atual do seu `README.md` por esse.
2. Em seguida, rode no terminal:

```bash
git add README.md
git commit -m "Atualiza README com explicação da reorganização e histórico preservado"
git push origin clean-start