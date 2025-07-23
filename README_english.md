# 🇺🇸 Read in English

# 💬 WhatsAppAutomation

This project automates message sending via **WhatsApp Web**, using **Python**, **Selenium**, and **Excel spreadsheets**.

---

## 📁 Project Structure

WhatsAppAutomation/

│

├── data/ # 📥 Input files (e.g., contatos.xlsx)

├── logs/ # 🧾 Execution logs and export files

├── src/ # ⚙️ Main scripts

│ ├── whatsapp_sender.py

│ ├── whatsapp_senderv1.py

│ ├── whatsapp_senderv2.py

│ └── ...

│

├── run_legacy.py # 🕹️ Run old scripts by name

├── requirements.txt # 📦 Project dependencies

├── setup.ps1 / .bat # ⚙️ Setup/Environment scripts

├── README.PO.md # 📘 Portuguese version

├── README.EN.md # 📗 This file (English)

└── README.md # 🌐 Main index with links

---

## 🧰 Requirements

- ✅ Python 3.10 or higher  
- ✅ Firefox installed  
- ✅ Geckodriver added to your PATH  
- ✅ Install dependencies with:

```bash
pip install -r requirements.txt
▶️ How to Run
Open your terminal and run:

python src/whatsapp_senderv2.py
📝 Features
Load contacts from .xlsx files

Send WhatsApp Web messages automatically

Create log reports per execution

Optionally export results to Excel

Run legacy scripts with run_legacy.py

🧪 Legacy Support
To run older scripts:

python run_legacy.py WhatsApp3.py

---

### 🔒 Disclaimer

This project is for educational purposes only.
Mass automation may violate WhatsApp's [Terms of Use](https://www.whatsapp.com/legal/terms-of-service).

---

### 📚 Credits

Developed by **Vinicius Teixeira**
