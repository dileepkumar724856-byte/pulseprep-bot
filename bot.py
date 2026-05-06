

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

# QUIZ DATA
quiz_data = [
    {
        "question": "Human heart has how many chambers?",
        "options": ["2", "3", "4", "5"],
        "answer": "4"
    },
    {
        "question": "DNA full form?",
        "options": [
            "Deoxyribo Nucleic Acid",
            "Dynamic Network Acid",
            "Double Nitrogen Acid",
            "None"
        ],
        "answer": "Deoxyribo Nucleic Acid"
    }
]

# MENU
MENU = [
    ["📚 Notes", "🧠 Test"],
    ["💎 Premium", "❓ Help"]
]

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to PulsePrep NEET Bot",
        reply_markup=ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    )

# SEND QUIZ
async def send_quiz(update, context):
    question = quiz_data[0]

    keyboard = []
    for option in question["options"]:
        keyboard.append(
            [InlineKeyboardButton(option, callback_data=option)]
        )

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"🧠 {question['question']}",
        reply_markup=reply_markup
    )

# HANDLE MENU
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "📚 Notes":
        await update.message.reply_text("📚 Notes coming soon")

    elif text == "🧠 Test":
        await send_quiz(update, context)

    elif text == "💎 Premium":
        await update.message.reply_text("💎 Premium soon")

    elif text == "❓ Help":
        await update.message.reply_text("Use buttons below 👇")

# QUIZ BUTTON
async def quiz_button(update, context):

    query = update.callback_query
    await query.answer()

    selected = query.data
    correct = quiz_data[0]["answer"]

    if selected == correct:
        await query.message.reply_text("✅ Correct Answer")
    else:
        await query.message.reply_text(f"❌ Wrong\nCorrect: {correct}")

# APP START
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)

app.add_handler(CallbackQueryHandler(quiz_button))

print("Bot Running...")

app.run_polling()
