import requests
from Dolar import buscar_cotacao_dolar
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN or not ID:
    raise ValueError("TELEGRAM_TOKEN ou TELEGRAM_CHAT_ID não definidos no .env")

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": ID,
        "text": mensagem
    }

    try:
        resposta = requests.post(url, data=payload, timeout=10)
        resposta.raise_for_status()
        print("Mensagem enviada!")
    except requests.exceptions.RequestException as e:
        print("Erro ao enviar mensagem:", e)

if __name__ == "__main__":
    cotacao = buscar_cotacao_dolar()
    mensagem = f"Cotação do dólar hoje:\nR$ {cotacao}"
    print(mensagem)
    enviar_telegram(mensagem)