from telebot import types
from bot import bot
from constants import ABOUT_ME_TEXT, TECH_STACK_TEXT, CONTACT_TEXT

# =====================
# /start, /help commands
# =====================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton("👨‍💻 About Me"),
        types.KeyboardButton("🛠 Tech Stack")
    )
    keyboard.add(
        types.KeyboardButton("💼 Projects"),
        types.KeyboardButton("📞 Contact")
    )

    bot.send_message(
        message.chat.id,
        "👋 Salom! Men *Asadbek Rakhimov*man\n"
        "⚡ Frontend Engineer | React.js & Next.js Specialist\n\n"
        "Quyidagi bo'limlardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=keyboard
    )


# =====================
# About Me
# =====================
@bot.message_handler(func=lambda m: m.text == "👨‍💻 About Me")
def about_me(message):
    bot.send_message(message.chat.id, ABOUT_ME_TEXT, parse_mode="Markdown")


# =====================
# Tech Stack
# =====================
@bot.message_handler(func=lambda m: m.text == "🛠 Tech Stack")
def tech_stack(message):
    bot.send_message(message.chat.id, TECH_STACK_TEXT, parse_mode="Markdown")


# =====================
# Contact
# =====================
@bot.message_handler(func=lambda m: m.text == "📞 Contact")
def contact(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("💼 LinkedIn", url="https://linkedin.com/in/asadbek-rakhimov"),
        types.InlineKeyboardButton("📱 Telegram", url="https://t.me/asadbekjs")
    )
    keyboard.add(
        types.InlineKeyboardButton("📧 Gmail", url="https://mail.google.com/mail/?view=cm&to=asadbekme2002@gmail.com"),
        types.InlineKeyboardButton("🌐 Portfolio", url="https://asadbekjs.uz")
    )
    keyboard.add(
        types.InlineKeyboardButton("📩 Leave a message", callback_data="leave_msg")
    )

    bot.send_message(
        message.chat.id,
        CONTACT_TEXT,
        parse_mode="Markdown",
        reply_markup=keyboard
    )
