
- 🇧🇷 [Leia em Português](README_portugues.md)


# WhatsAppAutomation 🇧🇷

Este projeto permite o envio automatizado de mensagens via WhatsApp Web utilizando Python, Selenium e planilhas Excel.

## Estrutura do Projeto

WhatsAppAutomation/
│
├── data/ # Arquivos de entrada, como contatos.xlsx
├── logs/ # Logs de execução e arquivos exportados
├── src/ # Scripts principais
│ ├── whatsapp_sender.py
│ ├── whatsapp_senderv1.py
│ ├── whatsapp_senderv2.py
│ └── ...
├── run_legacy.py # Executa scripts antigos por nome
├── requirements.txt # Dependências do projeto
├── setup.ps1/.bat # Scripts de instalação e ambiente
└── README.md # Versão principal do README

markdown
Copiar
Editar

## Requisitos

- Python 3.10+
- Firefox + Geckodriver
- Pacotes (via `pip install -r requirements.txt`)

## Executando

```bash
python src/whatsapp_sender.py

