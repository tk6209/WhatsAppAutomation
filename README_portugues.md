# 🇧🇷 Leia em Português

# 💬 WhatsAppAutomation

Este projeto permite o envio automatizado de mensagens via **WhatsApp Web** utilizando **Python**, **Selenium** e **planilhas Excel**.

---

## 📁 Estrutura do Projeto

WhatsAppAutomation/
│
├── data/ # 📥 Arquivos de entrada (ex: contatos.xlsx)
├── logs/ # 🧾 Logs de execução e arquivos exportados
├── src/ # ⚙️ Scripts principais
│ ├── whatsapp_sender.py
│ ├── whatsapp_senderv1.py
│ ├── whatsapp_senderv2.py
│ └── ...
│
├── run_legacy.py # 🕹️ Executa scripts antigos por nome
├── requirements.txt # 📦 Dependências do projeto
├── setup.ps1 / .bat # ⚙️ Scripts de instalação/ambiente
├── README.PO.md # 📘 Este arquivo (Português)
├── README.EN.md # 📗 Versão em inglês
└── README.md # 🌐 Versão principal com links

---

## 🧰 Requisitos

- ✅ Python 3.10 ou superior  
- ✅ Firefox instalado  
- ✅ Geckodriver no PATH  
- ✅ Instalar dependências com:

```bash
pip install -r requirements.txt
▶️ Como Executar
Abra o terminal e execute:

bash
Copiar
Editar
python src/whatsapp_senderv2.py
📝 Funcionalidades
Leitura de contatos via .xlsx

Envio automático de mensagens via WhatsApp Web

Log de envio por execução

Exportação opcional para Excel ao final

Execução de versões antigas com run_legacy.py

🧪 Testes e versões anteriores
Você pode rodar scripts antigos com:

bash
Copiar
Editar
python run_legacy.py WhatsApp3.py
🔒 Aviso
Este projeto é para fins educacionais. O uso em massa de automações pode violar os termos de uso do WhatsApp.

📚 Créditos
Desenvolvido por Vinicius Teixeira

📄 Leia também: README em Inglês 🇺🇸
