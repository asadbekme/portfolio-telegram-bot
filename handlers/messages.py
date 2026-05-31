from bot import bot, OWNER_ID
from constants import LEAVE_MSG_PROMPT

@bot.callback_query_handler(func=lambda call: call.data == "leave_msg")
def ask_for_message(call):
    bot.answer_callback_query(call.id)
    msg = bot.send_message(
        call.message.chat.id,
        LEAVE_MSG_PROMPT,
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
