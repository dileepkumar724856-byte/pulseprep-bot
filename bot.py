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

# MAIN MENU
MENU = [
    ["🧬 Biology", "⚡ Physics"],
    ["🧪 Chemistry", "🎲 Daily Quiz"],
    ["🏆 Leaderboard", "❓ Help"]
]

# QUESTION BANK
biology_questions = [

    {
        "question": "Powerhouse of cell?",
        "options": [
            "Nucleus",
            "Mitochondria",
            "Ribosome",
            "Golgi Body"
        ],
        "answer": 1,
        "explanation": "Mitochondria produces ATP energy."
    },

    {
        "question": "DNA full form?",
        "options": [
            "Deoxyribo Nucleic Acid",
            "Dynamic Network Acid",
            "Double Nitrogen Acid",
            "None"
        ],
        "answer": 0,
        "explanation": "DNA full form is Deoxyribo Nucleic Acid."
    }
]

physics_questions = [

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
        "question": "Speed of light?",
        "options": [
            "3×10^8 m/s",
            "5×10^8 m/s",
            "1×10^8 m/s",
            "7×10^8 m/s"
        ],
        "answer": 0,
        "explanation": "Speed of light is 3×10^8 m/s."
    }
]

chemistry_questions = [

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
    },

    {
        "question": "Atomic number of Carbon?",
        "options": [
            "6",
            "8",
            "12",
            "14"
        ],
        "answer": 0,
        "explanation": "Atomic number of carbon is 6."
    }
]

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
━━━━━━━━━━━━━━
🚀 PULSEPREP DAILY QUIZ BOT
━━━━━━━━━━━━━━

🧠 Daily Random Questions
📚 Subject Wise Practice
🏆 Leaderboard System

Choose Subject 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# SEND QUIZ
async def send_random_quiz(update, questions):

    q = random.choice(questions)

    await update.message.reply_poll(
        question=q["question"],
        options=q["options"],
        type="quiz",
        correct_option_id=q["answer"],
        explanation=q["explanation"]
    )

# HANDLE MENU
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    # BIOLOGY
    if text == "🧬 Biology":

        await send_random_quiz(
            update,
            biology_questions
        )

    # PHYSICS
    elif text == "⚡ Physics":

        await send_random_quiz(
            update,
            physics_questions
        )

    # CHEMISTRY
    elif text == "🧪 Chemistry":

        await send_random_quiz(
            update,
            chemistry_questions
        )

    # DAILY RANDOM QUIZ
    elif text == "🎲 Daily Quiz":

        all_questions = (
            biology_questions +
            physics_questions +
            chemistry_questions
        )

        await send_random_quiz(
            update,
            all_questions
        )

    # LEADERBOARD
    elif text == "🏆 Leaderboard":

        await update.message.reply_text(
            "🏆 Leaderboard Coming Soon"
        )

    # HELP
    elif text == "❓ Help":

        await update.message.reply_text(
            "Choose Subject Buttons 👇"
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
