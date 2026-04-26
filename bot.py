import os
import telebot
from google import genai

BOT_TOKEN = os.environ.get('BOT_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_KEY')

client = genai.Client(api_key=GEMINI_KEY)
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg: True)
def handle(msg):
    if msg.chat.type in ['group', 'supergroup']:
        if not (msg.text and f'@{bot.get_me().username}' in msg.text):
            return
        text = msg.text.replace(f'@{bot.get_me().username}', '').strip()
    else:
        text = msg.text
    response = client.models.generate_content(model='gemini-2.0-flash', contents=text)
    bot.reply_to(msg, response.text)

bot.polling()
