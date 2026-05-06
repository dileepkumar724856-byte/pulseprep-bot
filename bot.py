from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)

import os

TOKEN = os.getenv("TOKEN")

# CHANNEL USERNAME


# MAIN MENU
MENU = [
    ["🧬 Biology", "⚡ Physics"],
    ["🧪 Chemistry", "🏆 Leaderboard"],
    ["💎 Premium", "❓ Help"]
]

# FORCE JOIN CHECK


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user


    # WELCOME UI
    text = f"""
━━━━━━━━━━━━━━
🚀 PULSEPREP NEET BOT
━━━━━━━━━━━━━━

👋 Welcome {user.first_name}

📚 Notes
🧠 Daily Tests
🏆 Leaderboard
💎 Premium Access

Choose Subject Below 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# BIOLOGY QUIZ
async def biology_poll(update):

    await update.message.reply_poll(
        question="Which organelle is called powerhouse of cell?",
        options=[
            "Nucleus",
            "Mitochondria",
            "Ribosome",
            "Golgi Body"
        ],
        type="quiz",
        correct_option_id=1,
        explanation="Mitochondria produces ATP energy."
    )

# PHYSICS QUIZ
async def physics_poll(update):

    await update.message.reply_poll(
        question="SI unit of force is?",
        options=[
            "Joule",
            "Newton",
            "Pascal",
            "Watt"
        ],
        type="quiz",
        correct_option_id=1,
        explanation="Force SI unit is Newton."
    )

# CHEMISTRY QUIZ
async def chemistry_poll(update):

    await update.message.reply_poll(
        question="pH of neutral water is?",
        options=[
            "5",
            "7",
            "9",
            "14"
        ],
        type="quiz",
        correct_option_id=1,
        explanation="Neutral water pH is 7."
    )

# HANDLE BUTTONS
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    if text == "🧬 Biology":

        await biology_poll(update)

    elif text == "⚡ Physics":

        await physics_poll(update)

    elif text == "🧪 Chemistry":

        await chemistry_poll(update)

    elif text == "🏆 Leaderboard":

        await update.message.reply_text(
            "🏆 Leaderboard Coming Soon"
        )

    elif text == "💎 Premium":

        await update.message.reply_text(
            "💎 Premium System Coming Soon"
        )

    elif text == "❓ Help":

        await update.message.reply_text(
            "Use Subject Buttons To Start Quiz 👇"
        )

# BUILD APP
app = ApplicationBuilder().token(TOKEN).build()

# HANDLERS
app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    )
)

print("Bot Running...")

# RUN BOT
app.run_polling()
