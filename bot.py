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

from units_questions import units_questions

TOKEN = os.getenv("TOKEN")

# MENU
MENU = [
    ["⚡ Units & Dimensions"],
    ["🎲 Random Quiz"]
]

# STORE USED QUESTIONS
used_questions = []

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
━━━━━━━━━━━━━━
🚀 PULSEPREP PYQ BOT
━━━━━━━━━━━━━━

✅ No Repeat Questions
📚 Chapter Wise PYQs
🎲 Random Practice

Choose Option 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# NO REPEAT QUIZ
async def send_quiz(update):

    global used_questions

    # RESET IF ALL USED
    if len(used_questions) == len(units_questions):

        used_questions = []

    # AVAILABLE QUESTIONS
    remaining = []

    for q in units_questions:

        if q not in used_questions:

            remaining.append(q)

    # RANDOM PICK
    q = random.choice(remaining)

    # SAVE USED
    used_questions.append(q)

    # SEND POLL
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

    if text == "⚡ Units & Dimensions":

        await send_quiz(update)

    elif text == "🎲 Random Quiz":

        await send_quiz(update)

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
