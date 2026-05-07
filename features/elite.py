from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def elite_zone(update):

    keyboard = [

        [
            InlineKeyboardButton(
                "🧠 AI Mentor",
                callback_data="mentor"
            )
        ],

        [
            InlineKeyboardButton(
                "📚 AIR Notes Vault",
                callback_data="vault"
            )
        ],

        [
            InlineKeyboardButton(
                "🎯 Full Mock Tests",
                callback_data="mock"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = '''
━━━━━━━━━━━━━━
💎 ELITE ZONE
━━━━━━━━━━━━━━

🚀 Premium Dashboard
🔒 AIR Notes
🔒 AI Mentor
🔒 Full Tests

Choose Feature 👇
'''

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )
