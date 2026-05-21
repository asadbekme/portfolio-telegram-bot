import telebot
from telebot import types
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access variables
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

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
    text = (
        "👨‍💻 *About Me*\n"
        "━━━━━━━━━━━━━━━━\n\n"
        "💼 3+ yil davomida production-grade web ilovalar yaratib kelmoqdaman\n\n"
        "⚡ React.js, Next.js, TypeScript va zamonaviy frontend arxitekturasi bo'yicha tajribam bor\n\n"
        "🌱 Hozirda React Native va Python backend yo'nalishlarini o'rganmoqdaman\n\n"
        "🧠 Performance optimization, clean architecture va maintainable UI sistemalarga qiziqaman\n\n"
        "💬 React, TypeScript, Next.js, Python va frontend system design bo'yicha suhbatlashishga doim tayyorman"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")


# =====================
# Tech Stack
# =====================
@bot.message_handler(func=lambda m: m.text == "🛠 Tech Stack")
def tech_stack(message):
    text = (
        "🛠 *Tech Stack*\n"
        "━━━━━━━━━━━━━━━━\n\n"
        "🖥 *Frontend:*\n"
        "  • React.js, Next.js\n"
        "  • TypeScript, JavaScript\n\n"
        "🔄 *State Management:*\n"
        "  • Redux Toolkit\n"
        "  • TanStack Query\n\n"
        "🎨 *Styling:*\n"
        "  • Tailwind CSS\n"
        "  • Shadcn UI\n\n"
        "🗄 *Backend & DB:*\n"
        "  • Supabase\n"
        "  • Python (o'rganmoqdaman)\n\n"
        "🧰 *Tools:*\n"
        "  • Git, GitHub, VS Code\n"
        "  • Figma, Postman"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")


# =====================
# Projects
# =====================
@bot.message_handler(func=lambda m: m.text == "💼 Projects")
def projects(message):
    bot.send_message(
        message.chat.id,
        "💼 *Projects*\n"
        "━━━━━━━━━━━━━━━━\n\n"
        "Tez orada qo'shiladi... 🚧",
        parse_mode="Markdown"
    )


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

    text = (
        "📞 *Contact*\n"
        "━━━━━━━━━━━━━━━━\n\n"
        "💼 LinkedIn: [asadbek-rakhimov](https://linkedin.com/in/asadbek-rakhimov)\n"
        "📱 Telegram: [@asadbekjs](https://t.me/asadbekjs)\n"
        "📧 Gmail: asadbekme2002@gmail.com\n"
        "🌐 Portfolio: [asadbekjs.uz](https://asadbekjs.uz)\n\n"
        "📩 Istalgan vaqt bog'laning!"
    )
    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=keyboard
    )


bot.infinity_polling()