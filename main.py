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
PROJECTS = [
    {
        "id": "alif_market",
        "title": "Alif Market Group",
        "description": "Zamonaviy bizneslar uchun raqamli yechimlarni yaratish va amalga oshirishga ixtisoslashgan investitsiya kompaniyasi.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768809820766-q3szpk.png",
        "tech": ["React", "Next.js", "Tailwind CSS", "TypeScript", "Tanstack Query", "Headless UI"],
        "live_url": "https://aetestdomain.com",
        "github_url": "https://github.com/asadbekme"
    },
    {
        "id": "dieselly",
        "title": "Dieselly AI",
        "description": "Tejamkorlikni oshirish, haydashni optimallashtirish - avtopark va mustaqil avtomobillar uchun mo‘ljallangan yoqilg‘i kartasi muqobili.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768835532225-bppveq.png",
        "tech": ["React", "Next JS", "Tailwind CSS", "Shadcn UI", "Rest API", "Here Map", "TypeScript", "Zustand"],
        "live_url": "https://dieselly.ai",
        "github_url": "https://github.com/asadbekme"
    },
    {
        "id": "doner_food",
        "title": "Doner Food",
        "description": "Biz tezkor xizmat, mazali taom va do'stona muhitni taklif qilamiz. Bugun buyurtma bering va ta'mdan bahramand bo'ling!",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768835164338-nwpbeu.png",
        "tech": ["React", "Supabase", "TypeScript", "Shadcn UI", "Tailwind CSS", "PostgreSQL"],
        "live_url": "https://www.donerfood.uz",
        "github_url": "https://github.com/asadbekme/doner-food"
    },
    {
        "id": "task_manager",
        "title": "Vazifalarni boshqarish ilovasi",
        "description": "Aynan Kanban uslubidagi tortish va tashlash, vazifa ko'rinishlari va admin nazorati bilan zamonaviy vazifalarni boshqarish ilovasi.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768816741288-gfzhwi.webp",
        "tech": ["Next.js", "Shadcn UI", "Tailwind CSS", "TypeScript", "jsonstorage.net", "Tanstack Query"],
        "live_url": "https://task-management-app-by-asadbekjs.vercel.app",
        "github_url": "https://github.com/asadbekme/task-management-app"
    },
    {
        "id": "education_crm",
        "title": "Ta'lim CRM tizimi",
        "description": "Foydalanuvchi autentifikatsiyasi, rolga asoslangan kirish va moslashuvchan dizayn bilan ta'minlangan ta'lim muassasalari uchun keng qamrovli CRM tizimi.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768834310463-spj4cp.jpg",
        "tech": ["React", "Next.js", "Shadcn UI", "Tailwind CSS", "Typescript", "Recharts"],
        "live_url": "https://education-crm-flame.vercel.app",
        "github_url": "https://github.com/asadbekme/education-crm"
    },
    {
        "id": "glasses_shop",
        "title": "Ko'zoynak do'koni veb-sayti",
        "description": "Zamonaviy elektron kommeritsiya uchun elegant va moslashuvchan veb-sayt.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1768834630575-c5cwgu.png",
        "tech": ["HTML", "SASS", "JavaScript"],
        "live_url": "https://glasses-website-design.netlify.app",
        "github_url": "https://github.com/asadbekme/glasses-website-design"
    },
    {
        "id": "learnify",
        "title": "Learnify",
        "description": "O‘quv markazlari uchun marketing veb-saytlari va sahifalar tarkibini admin panelidan to‘liq boshqarish mumkin.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1772616881161-9khjhk.png",
        "tech": ["React", "Tailwind CSS", "Supabase", "Shadcn UI", "TypeScript", "Tanstack Query"],
        "live_url": "https://learnify-lc.vercel.app",
        "github_url": "https://github.com/asadbekme"
    },
    {
        "id": "inkwell",
        "title": "Inkwell",
        "description": "Inkwell - bu Medium’dan ilhomlangan, har qanday mavzuda hikoyalarni o‘qish va yozish uchun mo‘ljallangan zamonaviy, to‘liq stekli blog yuritish platformasi. Samaradorlik va SEOni hisobga olgan holda ishlab chiqilgan bo‘lib, u sahifalarni tez yuklash va optimal topiluvchanlikni ta’minlash uchun server tomonidagi renderlash (SSR) tizimidan foydalanadi.",
        "image": "https://zzrvmhxirmiemqxlflbt.supabase.co/storage/v1/object/public/project-images/projects/1777057456165-cculfi.png",
        "tech": ["React", "Vite", "TanStack Start", "TanStack Router", "Tailwind CSS", "Supabase", "Shadcn UI"],
        "live_url": "https://inkwell-app.asadbekme2002.workers.dev/",
        "github_url": "https://github.com/asadbekme"
    }
]

def get_projects_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for i, project in enumerate(PROJECTS):
        keyboard.add(types.InlineKeyboardButton(f"💻 {project['title']}", callback_data=f"proj_{i}"))
    return keyboard

@bot.message_handler(func=lambda m: m.text == "💼 Projects")
def projects(message):
    text = (
        "💼 *Loyihalarim*\n"
        "━━━━━━━━━━━━━━━━\n\n"
        "Quyidagi loyihalarimdan birini tanlang va u haqida batafsil ma'lumot oling:"
    )
    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=get_projects_keyboard()
    )

@bot.callback_query_handler(func=lambda call: call.data == "projects_list")
def show_projects_list_callback(call):
    bot.answer_callback_query(call.id)
    text = (
        "💼 *Loyihalarim*\n"
        "━━━━━━━━━━━━━━━━\n\n"
        "Quyidagi loyihalarimdan birini tanlang va u haqida batafsil ma'lumot oling:"
    )
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception:
        pass
    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=get_projects_keyboard()
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("proj_"))
def show_project_detail(call):
    bot.answer_callback_query(call.id)
    try:
        proj_idx = int(call.data.split("_")[1])
        project = PROJECTS[proj_idx]
    except (ValueError, IndexError):
        bot.send_message(call.message.chat.id, "❌ Loyiha topilmadi.")
        return

    # Create keyboard with links and back button
    keyboard = types.InlineKeyboardMarkup()
    buttons = []
    if project["live_url"]:
        buttons.append(types.InlineKeyboardButton("🌐 Live Demo", url=project["live_url"]))
    if project["github_url"]:
        buttons.append(types.InlineKeyboardButton("💻 GitHub", url=project["github_url"]))
    
    if buttons:
        # Add links in the first row
        keyboard.add(*buttons)
    
    keyboard.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="projects_list"))

    # Tech stack formatting
    tech_str = ", ".join(project["tech"])
    
    # Detail message caption
    caption_text = (
        f"*🚀 {project['title']}*\n"
        f"━━━━━━━━━━━━━━━━\n\n"
        f"📝 {project['description'].strip()}\n\n"
        f"🛠 *Texnologiyalar:* {tech_str}"
    )

    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception:
        pass

    # Send photo with details as caption
    bot.send_photo(
        call.message.chat.id,
        photo=project["image"],
        caption=caption_text,
        parse_mode="Markdown",
        reply_markup=keyboard
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