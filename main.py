import os
import requests
from telegram import Bot

# Telegram Bot Setup
TOKEN = os.getenv("TELEGRAM_TOKEN")   # Render env me set karo
CHAT_ID = os.getenv("TELEGRAM_CHAT")  # Render env me set karo
bot = Bot(token=TOKEN)

def get_signal():
    # Yahan apna analysis logic add karna (Price Action + Indicators)
    return "📈 UP signal on CRYPTO IDX (1m)"

def send_signal():
    signal = get_signal()
    bot.send_message(chat_id=CHAT_ID, text=signal)

if __name__ == "__main__":
    send_signal()
