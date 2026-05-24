import telebot
from telebot import types
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access variables
TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

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
    keyboard.add(
        types.InlineKeyboardButton("📩 Leave a message", callback_data="leave_msg")
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


# =====================
# Leave a message handler
# =====================
@bot.callback_query_handler(func=lambda call: call.data == "leave_msg")
def ask_for_message(call):
    bot.answer_callback_query(call.id)
    msg = bot.send_message(
        call.message.chat.id,
        "✍️ Iltimos, xabaringizni yozib yuboring. Men uni bot egasiga yetkazaman.\n\n"
        "*(Bekor qilish uchun /cancel deb yozing)*",
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(msg, process_message_step)


def process_message_step(message):
    # Handle cancellation
    if message.text and message.text.strip() == "/cancel":
        bot.send_message(message.chat.id, "❌ Xabar yuborish bekor qilindi.")
        return

    if not OWNER_ID:
        bot.send_message(
            message.chat.id,
            "⚠️ Hozircha xabar yuborib bo'lmaydi (tizim sozlanmagan). Keyinroq qayta urunib ko'ring."
        )
        return

    try:
        sender_name = message.from_user.first_name
        sender_username = f"@{message.from_user.username}" if message.from_user.username else "mavjud emas"
        sender_id = message.from_user.id

        info_text = (
            f"📩 *Yangi xabar!*\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"👤 *Kimdan:* {sender_name} ({sender_username})\n"
            f"🆔 *ID:* `{sender_id}`\n"
        )
        # Send info header first
        bot.send_message(OWNER_ID, info_text, parse_mode="Markdown")
        # Forward original message (preserves text formatting, images, media, stickers, etc.)
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)

        bot.send_message(message.chat.id, "✅ Xabaringiz muvaffaqiyatli yuborildi! Rahmat.")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Xabar yuborishda xatolik yuz berdi: {str(e)}")


bot.infinity_polling()