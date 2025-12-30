import telebot
import requests
from bs4 import BeautifulSoup

API_TOKEN = "8305876182:AAFzQZE6raBgGe33Y4w3l4zfl_HUqko2Bwo"   
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!")

@bot.message_handler(content_types=['text'])
def echo_handler(message):
    code = message.text.strip()
    url = f"https://aeroportix.ru/aeroport/{code}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    }

    resp = requests.get(url, headers=headers, timeout=20)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    block = soup.select_one(".texture-overlay #page #columns #block-system-main")

    text = block.get_text("\n", strip=True)

    bot.send_message(message.chat.id, text)

bot.infinity_polling()
