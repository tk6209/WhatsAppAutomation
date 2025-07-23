
- 🇺🇸 [Read in English](README_english.md)

# WhatsAppAutomation 🇺🇸

This project enables automated WhatsApp Web messaging using Python, Selenium, and Excel spreadsheets.

## Project Structure

WhatsAppAutomation/
│
├── data/ # Input files, like contatos.xlsx
├── logs/ # Execution logs and exported files
├── src/ # Main scripts
│ ├── whatsapp_sender.py
│ ├── whatsapp_senderv1.py
│ ├── whatsapp_senderv2.py
│ └── ...
├── run_legacy.py # Run legacy scripts by name
├── requirements.txt # Project dependencies
├── setup.ps1/.bat # Setup scripts
└── README.md # Main multilingual entry point

markdown
Copiar
Editar

## Requirements

- Python 3.10+
- Firefox + Geckodriver
- Packages (`pip install -r requirements.txt`)

## Run

```bash
python src/whatsapp_sender.py