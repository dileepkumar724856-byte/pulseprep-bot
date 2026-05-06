from telegram import (
    Update,
    ReplyKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

import os

TOKEN = os.getenv("TOKEN")

# MENU
MENU = [
    ["🧬 Biology", "⚡ Physics"],
    ["🧪 Chemistry", "🏆 Leaderboard"],
    ["💎 Premium", "❓ Help"]
]

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
━━━━━━━━━━━━━━
🚀 PULSEPREP NEET BOT
━━━━━━━━━━━━━━

📚 Notes
🧠 Daily Tests
🏆 Leaderboard
💎 Premium

Choose Subject 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# BIOLOGY
async def biology(update):

    # SEND PDF
    await update.message.reply_document(
        document=open("biology.pdf", "rb")
    )

    # SEND QUIZ
    await update.message.reply_poll(
        question="Powerhouse of cell?",
        options=[
            "Nucleus",
            "Mitochondria",
            "Golgi Body",
            "Ribosome"
        ],
        type="quiz",
        correct_option_id=1,
        explanation="Mitochondria produces ATP."
    )

# PHYSICS
async def physics(update):

    await update.message.reply_document(
        document=open("physics.pdf", "rb")
    )

    await update.message.reply_poll(
        question="SI unit of force?",
        options=[
            "Newton",
            "Joule",
            "Pascal",
            "Watt"
        ],
        type="quiz",
        correct_option_id=0,
        explanation="SI unit of force is Newton."
    )

# CHEMISTRY
async def chemistry(update):

    await update.message.reply_document(
        document=open("chemistry.pdf", "rb")
    )

    await update.message.reply_poll(
        question="pH of neutral water?",
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

        await biology(update)

    elif text == "⚡ Physics":

        await physics(update)

    elif text == "🧪 Chemistry":

        await chemistry(update)

    elif text == "🏆 Leaderboard":

        await update.message.reply_text(
            "🏆 Leaderboard Coming Soon"
        )

    elif text == "💎 Premium":

        await update.message.reply_text(
            "💎 Premium Coming Soon"
        )

    elif text == "❓ Help":

        await update.message.reply_text(
            "Choose Any Subject Button 👇"
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
