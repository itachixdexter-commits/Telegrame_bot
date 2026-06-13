import telebot
import requests
import os

TOKEN = os.getenv("8736816349:AAFOx4pyH92Tr5Jv6DDAF-fQcw3dF42nI6U")
bot = telebot.TeleBot(TOKEN)

user_state = {}

# /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("👤 المطور", "🌐 تحميل HTML")

    bot.send_message(message.chat.id, "مرحبا 👋 اختر:", reply_markup=markup)

# زر المطور
@bot.message_handler(func=lambda m: (m.text or "").strip() == "👤 المطور")
def dev(message):
    bot.send_message(message.chat.id, "ziko_f7l")

# زر تحميل HTML
@bot.message_handler(func=lambda m: (m.text or "").strip() == "🌐 تحميل HTML")
def ask_url(message):
    bot.send_message(message.chat.id, "ارسل رابط الموقع (لازم https):")
    user_state[message.chat.id] = "wait"

# استقبال الرابط
@bot.message_handler(func=lambda m: m.chat.id in user_state and user_state[m.chat.id] == "wait")
def get_html(message):
    chat_id = message.chat.id
    url = (message.text or "").strip()

    try:
        r = requests.get(url, timeout=10)

        with open("site.html", "w", encoding="utf-8") as f:
            f.write(r.text)

        with open("site.html", "rb") as f:
            bot.send_document(chat_id, f)

    except:
        bot.send_message(chat_id, "❌ خطأ في الرابط أو الموقع لا يستجيب")

    user_state.pop(chat_id, None)

# تشغيل البوت
bot.polling(none_stop=True)
