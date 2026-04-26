import os
import telebot
import google.generativeai as genai

BOT_TOKEN = os.environ.get('BOT_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_KEY')

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg: True)
def handle(msg):
    if msg.chat.type in ['group', 'supergroup']:
        if not (msg.text and f'@{bot.get_me().username}' in msg.text):
            return
        text = msg.text.replace(f'@{bot.get_me().username}', '').strip()
    else:
        text = msg.text
    
    reply = model.generate_content(text).text
    bot.reply_to(msg, reply)

bot.polling()
