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
import random
from features.leaderboard import leaderboard
from features.quiz import send_quiz

from features.elite import elite_zone

from questions.units_questions import units_questions

TOKEN = os.getenv("TOKEN")

# MAIN MENU
MENU = [
    ["⚡ Units & Dimensions", "🎯 Daily Challenge"],
    ["📚 Notes Hub", "🏆 AIR Leaderboard"],
    ["🔥 My Streak", "💎 Elite Zone"]
]

# USER DATA
user_xp = {}
user_streak = {}

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.first_name

    text = f"""
━━━━━━━━━━━━━━━━━━
⚡ PULSEPREP ELITE ⚡
━━━━━━━━━━━━━━━━━━

👋 Welcome {user}

🎯 Daily Challenges
📚 Chapter Wise PYQs
🏆 AIR Leaderboard
🔥 XP & Streak System
💎 Elite Dashboard

Choose Option 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# QUIZ


# DAILY CHALLENGE
async def daily_challenge(update):

    text = """
🔥 DAILY CHALLENGE 🔥

🎯 Solve 5 MCQs
⭐ Reward = +50 XP
🏆 Beat Other Students
"""

    await update.message.reply_text(text)

    await send_quiz(update)

# NOTES HUB
async def notes_hub(update):

    text = """
📚 NOTES HUB

⚡ Physics Notes
🧬 Biology Notes
🧪 Chemistry Notes

🔥 PYQ Notes
🧠 Formula Sheets
📘 Short Notes
"""

    await update.message.reply_text(text)

# LEADERBOARD
await leaderboard(update, user_xp)
# ELITE ZONE


# ELITE BUTTONS
async def elite_buttons(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data

    # AI MENTOR
    if data == "mentor":

        await query.message.reply_text(
            """
🧠 AI MENTOR

🚀 Ask Your NEET Doubts
📚 Smart Explanations
⚡ Fast Learning

Feature Coming Soon...
"""
        )

    # VAULT
    elif data == "vault":

        await query.message.reply_text(
            """
📚 AIR NOTES VAULT

🔒 Topper Notes
🔒 Formula Sheets
🔒 PYQ PDFs
🔒 Revision Notes

Elite Notes Coming Soon...
"""
        )

    # MOCK TEST
    elif data == "mock":

        await query.message.reply_text(
            """
🎯 FULL MOCK TESTS

⚡ Physics Test
🧪 Chemistry Test
🧬 Biology Test

🚀 NEET Simulation Mode
"""
        )

    # RANK BOOSTER
    elif data == "rank":

        await query.message.reply_text(
            """
📊 RANK BOOSTER

📈 Accuracy Tracking
📉 Weak Topic Analysis
🏆 AIR Strategy

Coming Soon...
"""
        )

    # DAILY MISSION
    elif data == "mission":

        await query.message.reply_text(
            """
🔥 DAILY MISSION

🎯 Solve 20 MCQs
⭐ Reward = +100 XP
🏆 Maintain Your Streak
"""
        )

# HANDLE MENU
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    user_id = update.effective_user.id

    # CREATE USER
    if user_id not in user_xp:

        user_xp[user_id] = 0

    if user_id not in user_streak:

        user_streak[user_id] = 1

    # UNITS QUIZ
    if text == "⚡ Units & Dimensions":

        user_xp[user_id] += 10

        await send_quiz(update)

    # DAILY CHALLENGE
    elif text == "🎯 Daily Challenge":

        user_xp[user_id] += 20

        user_streak[user_id] += 1

        await daily_challenge(update)

    # NOTES
    elif text == "📚 Notes Hub":

        await notes_hub(update)

    # LEADERBOARD
    elif text == "🏆 AIR Leaderboard":

        await leaderboard(update)

    # STREAK
    elif text == "🔥 My Streak":

        await streak(update)

    # ELITE ZONE
    elif text == "💎 Elite Zone":

        await elite_zone(update)

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
    CallbackQueryHandler(elite_buttons)
)

print("⚡ PulsePrep Elite Running...")

# RUN BOT
app.run_polling()
