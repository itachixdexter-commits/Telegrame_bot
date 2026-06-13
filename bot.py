import telebot
import requests

TOKEN = "8736816349:AAFOx4pyH92Tr5Jv6DDAF-fQcw3dF42nI6U"
bot = telebot.TeleBot(TOKEN)

user_state = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("👤 المطور", "🌐 تحميل HTML")

    bot.send_message(message.chat.id, "مرحبا 👋 اختر:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle(message):
    chat_id = message.chat.id
    text = message.text

    if text == "👤 المطور":
        bot.send_message(chat_id, "ziko_f7l")

    elif text == "🌐 تحميل HTML":
        bot.send_message(chat_id, "ارسل رابط الموقع:")
        user_state[chat_id] = "wait"

    elif chat_id in user_state and user_state[chat_id] == "wait":
        try:
            r = requests.get(text)
            open("site.html", "w", encoding="utf-8").write(r.text)

            bot.send_document(chat_id, open("site.html", "rb"))

        except:
            bot.send_message(chat_id, "خطأ في الرابط")

        user_state.pop(chat_id, None)

bot.polling()