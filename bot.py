import telebot
from telebot import types

# Bot tokeningizni shu yerga qo'yasiz
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📕 PDF")
    btn2 = types.KeyboardButton("🖼️ Rasmlar")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        "Salom! Men Fizika masalalar botiman.\nQuyidagilardan birini tanlang 👇",
        reply_markup=markup
    )

# Tugmalarni ishlatish
@bot.message_handler(func=lambda message: True)
def send_files(message):
    if message.text == "📕 PDF":
        bot.send_document(message.chat.id, open("fizika_masalalar_yangi_qoshimcha (2).pdf", "rb"))

    elif message.text == "🖼️ Rasmlar":
        photos = ["rasim1.jpg", "rasim2.jpg", "rasim3.jpg"]
        for photo in photos:
            with open(photo, "rb") as img:
                bot.send_photo(message.chat.id, img)

print("Bot ishlamoqda...")
bot.polling()
