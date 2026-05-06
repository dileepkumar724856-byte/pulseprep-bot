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

TOKEN = os.getenv("TOKEN")

# MENU
MENU = [
    ["🎲 Random Question", "🤖 AI Doubt"],
    ["🧬 Biology", "⚡ Physics"],
    ["🧪 Chemistry", "❓ Help"]
]

# RANDOM QUESTIONS
questions = [

    {
        "question": "SI unit of force?",
        "options": [
            "Newton",
            "Joule",
            "Pascal",
            "Watt"
        ],
        "answer": 0,
        "explanation": "SI unit of force is Newton."
    },

    {
        "question": "Powerhouse of cell?",
        "options": [
            "Nucleus",
            "Mitochondria",
            "Golgi Body",
            "Ribosome"
        ],
        "answer": 1,
        "explanation": "Mitochondria produces ATP."
    },

    {
        "question": "pH of neutral water?",
        "options": [
            "5",
            "7",
            "9",
            "14"
        ],
        "answer": 1,
        "explanation": "Neutral water pH is 7."
    }
]

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
━━━━━━━━━━━━━━
🚀 PULSEPREP AI BOT
━━━━━━━━━━━━━━

🎲 Random Questions
🤖 AI Doubt Solving
📚 Subject Tests

Choose Option 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# RANDOM QUIZ
async def random_quiz(update):

    q = random.choice(questions)

    await update.message.reply_poll(
        question=q["question"],
        options=q["options"],
        type="quiz",
        correct_option_id=q["answer"],
        explanation=q["explanation"]
    )

# AI DOUBT SOLVER
async def ai_reply(update):

    text = update.message.text.lower()

    # BIOLOGY
    if "mitochondria" in text:

        await update.message.reply_text(
            "🧬 Mitochondria is called powerhouse of cell because it produces ATP energy."
        )

    elif "dna" in text:

        await update.message.reply_text(
            "🧬 DNA full form is Deoxyribo Nucleic Acid."
        )

    # PHYSICS
    elif "force" in text:

        await update.message.reply_text(
            "⚡ Force = mass × acceleration\nSI unit = Newton"
        )

    # CHEMISTRY
    elif "ph" in text:

        await update.message.reply_text(
            "🧪 Neutral water has pH 7."
        )

    else:

        await update.message.reply_text(
            "🤖 AI is learning...\nTry NEET related doubts."
        )

# HANDLE BUTTONS
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    if text == "🎲 Random Question":

        await random_quiz(update)

    elif text == "🤖 AI Doubt":

        await update.message.reply_text(
            "🤖 Send your NEET doubt."
        )

    elif text == "🧬 Biology":

        await random_quiz(update)

    elif text == "⚡ Physics":

        await random_quiz(update)

    elif text == "🧪 Chemistry":

        await random_quiz(update)

    elif text == "❓ Help":

        await update.message.reply_text(
            "Use buttons below 👇"
        )

    else:

        await ai_reply(update)

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
