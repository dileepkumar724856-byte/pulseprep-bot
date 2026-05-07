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

🎯 Daily NEET Challenges
📚 Chapter Wise PYQs
🏆 AIR Style Leaderboard
🔥 Streak & XP System
💎 Elite Experience

Choose Option Below 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# SEND QUIZ
async def send_quiz(update):

    q = random.choice(units_questions)

    await update.message.reply_poll(
        question=f"⚡ {q['question']}\n\n📘 {q['year']}",
        options=q["options"],
        type="quiz",
        correct_option_id=q["answer"],
        explanation=f"✅ {q['explanation']}",
        is_anonymous=False
    )

# DAILY CHALLENGE
async def daily_challenge(update):

    await update.message.reply_text(
        """
🔥 DAILY CHALLENGE 🔥

🎯 Complete 5 MCQs Today
⭐ Reward = +50 XP
🏆 Beat Other Students
"""
    )

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

More Notes Coming Soon...
"""

    await update.message.reply_text(text)

# LEADERBOARD
async def leaderboard(update):

    if not user_xp:

        await update.message.reply_text(
            "🏆 No Students Yet"
        )

        return

    sorted_users = sorted(
        user_xp.items(),
        key=lambda x: x[1],
        reverse=True
    )

    text = "🏆 AIR LEADERBOARD 🏆\n\n"

    rank = 1

    for user_id, xp in sorted_users[:5]:

        text += f"{rank}. User {user_id} → {xp} XP\n"

        rank += 1

    await update.message.reply_text(text)

# STREAK
async def streak(update):

    user_id = update.effective_user.id

    streak = user_streak.get(user_id, 0)

    await update.message.reply_text(
        f"""
🔥 YOUR STREAK 🔥

⚡ Current Streak: {streak} Days
⭐ Keep Practicing Daily
"""
    )

# ELITE ZONE
async def elite_zone(update):

    text = """
💎 ELITE ZONE 💎

🔒 AIR Batch
🔒 Elite Notes
🔒 Full Mock Tests
🔒 AI Mentor

🚀 Premium Features Coming Soon
"""

    await update.message.reply_text(text)

# HANDLE BUTTONS
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

print("⚡ PulsePrep Elite Running...")

# RUN BOT
app.run_polling()
