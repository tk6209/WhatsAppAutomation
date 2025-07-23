import time
import logging
import pyautogui as pi
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urllib.parse import quote

# Setup de log
logging.basicConfig(
    filename='logs/envio_whatsapp.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def carregar_contatos(caminho_excel):
    try:
        df = pd.read_excel(caminho_excel)
        contatos = df.to_dict(orient='records')
        logging.info(f"{len(contatos)} contatos carregados com sucesso.")
        return contatos
    except Exception as e:
        logging.error(f"Erro ao carregar contatos: {e}")
        return []

def iniciar_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Firefox(options=options)

def enviar_mensagens(driver, contatos):
    for contato in contatos:
        telefone = str(contato["telefone"])
        mensagem = str(contato["mensagem"])

        if not telefone or not mensagem:
            logging.warning(f"Contato com dados incompletos: {contato}")
            continue

        url = f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"
        try:
            driver.get(url)
            logging.info(f"Abrindo conversa com {telefone}")
            time.sleep(5)
            pi.press('enter')
            time.sleep(1.5)
            pi.press('enter')
            logging.info(f"Mensagem enviada para {telefone}")
        except Exception as e:
            logging.error(f"Erro ao enviar para {telefone}: {e}")

def main():
    logging.info("Iniciando envio de mensagens via WhatsApp")
    contatos = carregar_contatos("data/contatos.xlsx")
    if not contatos:
        logging.error("Nenhum contato carregado. Encerrando.")
        return

    driver = iniciar_driver()
    driver.get("https://web.whatsapp.com")
    input("🔑 Escaneie o QR Code e pressione ENTER para continuar...")

    enviar_mensagens(driver, contatos)
    driver.quit()
    logging.info("Processo concluído com sucesso.")

if __name__ == "__main__":
    main()
