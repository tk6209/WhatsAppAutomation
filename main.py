import logging
from datetime import datetime

# Configuração básica do logger
logging.basicConfig(
    filename='logs/whatsapp_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def carregar_contatos():
    """
    Simula a leitura de contatos de um arquivo ou fonte externa.
    """
    contatos = [
        {"nome": "João", "telefone": "+551199999999"},
        {"nome": "Maria", "telefone": "+551198888888"}
    ]
    logging.info(f"{len(contatos)} contatos carregados com sucesso.")
    return contatos

def enviar_mensagem(contato, mensagem):
    """
    Simula o envio de uma mensagem para um contato.
    """
    logging.info(f"Enviando mensagem para {contato['nome']} ({contato['telefone']})")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Mensagem enviada para {contato['nome']}: {mensagem}")

def main():
    logging.info("Automação WhatsApp iniciada.")

    contatos = carregar_contatos()
    mensagem = "Olá! Esta é uma mensagem automática de teste 😊"

    for contato in contatos:
        enviar_mensagem(contato, mensagem)

    logging.info("Automação finalizada com sucesso.")

if __name__ == "__main__":
    main()
