from telebot import types
from bot import bot
from data.projects import PROJECTS, get_projects_keyboard
from constants import PROJECTS_HEADER_TEXT

@bot.message_handler(func=lambda m: m.text == "💼 Projects")
def projects(message):
    bot.send_message(
        message.chat.id,
        PROJECTS_HEADER_TEXT,
        parse_mode="Markdown",
        reply_markup=get_projects_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == "projects_list")
def show_projects_list_callback(call):
    bot.answer_callback_query(call.id)
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception:
        pass
    bot.send_message(
        call.message.chat.id,
        PROJECTS_HEADER_TEXT,
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
    if project.get("live_url"):
        buttons.append(types.InlineKeyboardButton("🌐 Live Demo", url=project["live_url"]))
    if project.get("github_url"):
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
