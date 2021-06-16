import telebot
import time

bot_token = '1869770648:AAHYUzR11CXPmZMRJF21PvnFu06W_lC7MF4'

bot = telebot.TeleBot(token=bot_token)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text


@bot.message_handler(commands=['start'])

def send_welcome(message):
    bot.reply_to(message, 'Welcome')

@bot.message_handler(commands=['help'])

def send_welcome(message):
    bot.reply_to(message, 'Send commands starting with "/"')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)
    bot.reply_to(message, "https://www.instagram.com/{}".format(at_text[1:]))


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
