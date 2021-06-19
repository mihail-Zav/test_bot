import telebot
import time
import os
from flask import Flask,request

bot_token = '1869770648:AAHYUzR11CXPmZMRJF21PvnFu06W_lC7MF4'
bot = telebot.TeleBot(token=bot_token)
server = Flask(__name__)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Send commands starting with "/". Test 123')

@bot.message_handler(func = lambda m: True)
def echo_meddage(message):
    bot.reply_to(message, message.text)

@bot.message_handler(func=lambda msg: msg.content_type == "photo")
def echo_photo(message):
    # fileID = message.photo[-1].file_id
    # file = bot.get_file(fileID)
    # bot.reply_to(message, file)
    bot.reply_to(message, "Thats a photo")

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)
    bot.reply_to(message, "https://www.instagram.com/{}".format(at_text[1:]))


@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://simple-bot-1.herokuapp.com/' + bot_token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


# while True:
#     try:
#         bot.polling()
#     except Exception:
#         time.sleep(15)
