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

⚡ Current Streak: {streak}
⭐ Keep Practicing Daily
"""
    )

# ELITE ZONE
async def elite_zone(update):

    keyboard = [

        [
            InlineKeyboardButton(
                "🧠 AI Mentor",
                callback_data="mentor"
            )
        ],

        [
            InlineKeyboardButton(
                "📚 AIR Notes Vault",
                callback_data="vault"
            )
        ],

        [
            InlineKeyboardButton(
                "🎯 Full Mock Tests",
                callback_data="mock"
            )
        ],

        [
            InlineKeyboardButton(
                "📊 Rank Booster",
                callback_data="rank"
            )
        ],

        [
            InlineKeyboardButton(
                "🔥 Daily Mission",
                callback_data="mission"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
━━━━━━━━━━━━━━
💎 ELITE ZONE
━━━━━━━━━━━━━━

🚀 Premium Student Dashboard

🔒 AIR Notes
🔒 Full Mock Tests
🔒 AI Mentor
🔒 Rank Booster

Choose Elite Feature 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

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
