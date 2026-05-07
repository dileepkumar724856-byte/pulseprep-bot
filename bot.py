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

# IMPORT FEATURES
from features.quiz import send_quiz, send_leader_test
from features.elite import elite_zone
from features.notes import notes_hub
from features.leaderboard import leaderboard

TOKEN = os.getenv("TOKEN")

# MENU
MENU = [
    ["⚡ Units & Dimensions", "🎯 Daily Challenge"],
    ["📚 Notes Hub", "🏆 AIR Leaderboard"],
    ["🔥 My Streak", "💎 Elite Zone"],
    ["🔥 LEADER TEST"]
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

# STREAK
async def streak(update):

    user_id = update.effective_user.id

    streak_count = user_streak.get(user_id, 0)

    text = f"""
🔥 YOUR STREAK 🔥

⚡ Current Streak: {streak_count}
⭐ Keep Practicing Daily
"""

    await update.message.reply_text(text)

# ELITE BUTTONS
async def elite_buttons(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "mentor":

        await query.message.reply_text(
            """
🧠 AI MENTOR

🚀 Ask Your NEET Doubts
📚 Smart Explanations
⚡ Fast Learning

Coming Soon...
"""
        )

    elif data == "vault":

        await query.message.reply_text(
            """
📚 AIR NOTES VAULT

🔒 Topper Notes
🔒 Formula Sheets
🔒 PYQ PDFs

Coming Soon...
"""
        )

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

    # NOTES HUB
    elif text == "📚 Notes Hub":

        await notes_hub(update)

    # LEADERBOARD
    elif text == "🏆 AIR Leaderboard":

        await leaderboard(update, user_xp)

    # STREAK
    elif text == "🔥 My Streak":

        await streak(update)

    # ELITE ZONE
    elif text == "💎 Elite Zone":

        await elite_zone(update)

    # LEADER TEST
    elif text == "🔥 LEADER TEST":

        await send_leader_test(update)

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
