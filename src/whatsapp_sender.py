import os
import time
import logging
import pyautogui as pi
import pandas as pd
from tqdm import tqdm
from urllib.parse import quote
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 🕒 Gera nome de log e exportação
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_path = f"logs/envio_{timestamp}.log"
export_path = f"logs/export_envio_{timestamp}.xlsx"

# 📜 Configuração do log
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

resultados = []

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
    for contato in tqdm(contatos, desc="Enviando mensagens", colour="green"):
        telefone = str(contato["telefone"])
        mensagem = str(contato["mensagem"])
        nome = contato.get("nome", "Desconhecido")
        status = "Não enviado"

        if not telefone or not mensagem:
            status = "Dados incompletos"
            logging.warning(f"Contato com dados incompletos: {contato}")
        else:
            url = f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"
            try:
                driver.get(url)
                logging.info(f"Abrindo conversa com {nome} ({telefone})")

                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
                )

                time.sleep(1.5)
                pi.press('enter')
                time.sleep(1.2)
                pi.press('enter')

                status = "Enviado"
                logging.info(f"✅ Mensagem enviada para {nome} ({telefone}) → \"{mensagem}\"")
            except Exception as e:
                status = f"Erro: {e}"
                logging.error(f"❌ Erro ao enviar para {telefone}: {e}")

        resultados.append({
            "nome": nome,
            "telefone": telefone,
            "mensagem": mensagem,
            "status": status
        })

def main():
    logging.info("▶️ Iniciando envio de mensagens via WhatsApp")
    contatos = carregar_contatos("data/contatos.xlsx")
    if not contatos:
        logging.error("Nenhum contato carregado. Encerrando.")
        return

    driver = iniciar_driver()
    driver.get("https://web.whatsapp.com")
    input("🔑 Escaneie o QR Code e pressione ENTER para continuar...")

    enviar_mensagens(driver, contatos)
    driver.quit()
    logging.info("✅ Processo concluído com sucesso.")

    # 📦 Perguntar se deseja exportar
    resposta = input("\nDeseja exportar um relatório Excel com os resultados? (s/n): ").strip().lower()
    if resposta == "s":
        df_resultado = pd.DataFrame(resultados)
        df_resultado.to_excel(export_path, index=False)
        print(f"\n📁 Relatório salvo em: {export_path}")
        logging.info(f"📁 Relatório salvo em: {export_path}")
    else:
        print("Relatório não gerado.")

if __name__ == "__main__":
    main()
