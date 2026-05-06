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
import random

# IMPORT QUESTIONS
from units_questions import units_questions

TOKEN = os.getenv("TOKEN")

# MENU
MENU = [
    ["⚡ Units & Dimensions"],
    ["🎲 Random Quiz"],
    ["🏆 Leaderboard"]
]

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
━━━━━━━━━━━━━━
🚀 PULSEPREP PHYSICS PYQ BOT
━━━━━━━━━━━━━━

📚 Chapter Wise PYQs
🎲 Random Practice
🏆 Leaderboard

Choose Option 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# SEND QUIZ
async def send_quiz(update, questions):

    q = random.choice(questions)

    await update.message.reply_poll(
        question=f"{q['question']}\n\n📘 {q['year']}",
        options=q["options"],
        type="quiz",
        correct_option_id=q["answer"],
        explanation=q["explanation"]
    )

# HANDLE BUTTONS
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    # UNITS & DIMENSIONS
    if text == "⚡ Units & Dimensions":

        await send_quiz(
            update,
            units_questions
        )

    # RANDOM QUIZ
    elif text == "🎲 Random Quiz":

        await send_quiz(
            update,
            units_questions
        )

    # LEADERBOARD
    elif text == "🏆 Leaderboard":

        await update.message.reply_text(
            "🏆 Leaderboard Coming Soon"
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
