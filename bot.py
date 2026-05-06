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

TOKEN = os.getenv("TOKEN")

# QUIZ QUESTIONS
quiz_data = [
    {
        "question": "Human heart has how many chambers?",
        "options": ["2", "3", "4", "5"],
        "answer": "4"
    }
]

# STATS
correct_count = 0
wrong_count = 0

# MENU
MENU = [
    ["📚 Notes", "🧠 Test"],
    ["💎 Premium", "❓ Help"]
]

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🚀 Welcome to PulsePrep NEET Bot",
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# SEND QUIZ
async def send_quiz(message, context):

    question = quiz_data[0]

    keyboard = []

    for option in question["options"]:

        keyboard.append([
            InlineKeyboardButton(
                option,
                callback_data=option
            )
        ])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await message.reply_text(
        f"🧠 {question['question']}",
        reply_markup=reply_markup
    )

# HANDLE MENU
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    if text == "📚 Notes":

        await update.message.reply_text(
            "📚 Notes coming soon"
        )

    elif text == "🧠 Test":

        await send_quiz(
            update.message,
            context
        )

    elif text == "💎 Premium":

        await update.message.reply_text(
            "💎 Premium coming soon"
        )

    elif text == "❓ Help":

        await update.message.reply_text(
            "Use menu buttons below 👇"
        )

# QUIZ ANSWER
async def quiz_button(update, context):

    global correct_count
    global wrong_count

    query = update.callback_query

    await query.answer()

    selected = query.data

    correct = quiz_data[0]["answer"]

    if selected == correct:

        correct_count += 1

        await query.message.reply_text(
            "✅ Correct Answer"
        )

    else:

        wrong_count += 1

        await query.message.reply_text(
            f"❌ Wrong Answer\n✅ Correct: {correct}"
        )

    total = correct_count + wrong_count

    correct_percent = (correct_count / total) * 100
    wrong_percent = (wrong_count / total) * 100

    await query.message.reply_text(
        f"📊 Students Statistics\n\n"
        f"✅ Correct: {correct_count} ({correct_percent:.1f}%)\n"
        f"❌ Wrong: {wrong_count} ({wrong_percent:.1f}%)"
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
    CallbackQueryHandler(quiz_button)
)

print("Bot Running...")

# RUN BOT
app.run_polling()
