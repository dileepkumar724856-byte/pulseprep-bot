from telegram import (
    Update,
    ReplyKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    PollAnswerHandler,
    filters,
    ContextTypes
)

import os
import random

TOKEN = os.getenv("TOKEN")

# MENU
MENU = [
    ["🧬 Biology", "⚡ Physics"],
    ["🧪 Chemistry", "🎲 Daily Quiz"],
    ["🏆 Leaderboard", "🔥 My Streak"]
]

# USER DATA
user_scores = {}
user_streaks = {}

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
        "explanation": "Mitochondria produces ATP."
    }

]

physics_questions = [

    {
        "question": "SI unit of force?",
        "options": [
            "Newton",
            "Joule",
            "Watt",
            "Pascal"
        ],
        "answer": 0,
        "explanation": "SI unit of force is Newton."
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
    }

]

# STORE ACTIVE POLLS
active_polls = {}

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
━━━━━━━━━━━━━━
🚀 PULSEPREP QUIZ BOT
━━━━━━━━━━━━━━

🧠 Daily Practice
🏆 Leaderboard
🔥 Streak System

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
async def send_quiz(update, questions):

    q = random.choice(questions)

    message = await update.message.reply_poll(
        question=q["question"],
        options=q["options"],
        type="quiz",
        correct_option_id=q["answer"],
        explanation=q["explanation"],
        is_anonymous=False
    )

    active_polls[message.poll.id] = q

# HANDLE POLL ANSWERS
async def receive_poll_answer(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    answer = update.poll_answer

    user_id = answer.user.id

    poll_id = answer.poll_id

    selected = answer.option_ids[0]

    if user_id not in user_scores:
        user_scores[user_id] = 0

    if user_id not in user_streaks:
        user_streaks[user_id] = 0

    if poll_id in active_polls:

        correct = active_polls[poll_id]["answer"]

        # CORRECT ANSWER
        if selected == correct:

            user_scores[user_id] += 1

            user_streaks[user_id] += 1

# HANDLE BUTTONS
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    # BIOLOGY
    if text == "🧬 Biology":

        await send_quiz(
            update,
            biology_questions
        )

    # PHYSICS
    elif text == "⚡ Physics":

        await send_quiz(
            update,
            physics_questions
        )

    # CHEMISTRY
    elif text == "🧪 Chemistry":

        await send_quiz(
            update,
            chemistry_questions
        )

    # DAILY QUIZ
    elif text == "🎲 Daily Quiz":

        all_questions = (
            biology_questions +
            physics_questions +
            chemistry_questions
        )

        await send_quiz(
            update,
            all_questions
        )

    # LEADERBOARD
    elif text == "🏆 Leaderboard":

        if not user_scores:

            await update.message.reply_text(
                "No quiz attempts yet."
            )

            return

        sorted_users = sorted(
            user_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        text_data = "🏆 Leaderboard\n\n"

        rank = 1

        for user_id, score in sorted_users[:5]:

            text_data += (
                f"{rank}. User {user_id} → {score} points\n"
            )

            rank += 1

        await update.message.reply_text(
            text_data
        )

    # STREAK
    elif text == "🔥 My Streak":

        user_id = update.effective_user.id

        streak = user_streaks.get(user_id, 0)

        await update.message.reply_text(
            f"🔥 Your Current Streak: {streak}"
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

app.add_handler(
    PollAnswerHandler(receive_poll_answer)
)

print("Bot Running...")

# RUN BOT
app.run_polling()
