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
        "🚀 Welcome to PulsePrep NEET",
        reply_markup=ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    )

# SEND QUIZ
async def send_quiz(update, context, q_index=0):

    question = quiz_data[q_index]

    keyboard = []

    for option in question["options"]:
        keyboard.append(
            [InlineKeyboardButton(option, callback_data=f"{q_index}|{option}")]
        )

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"🧠 {question['question']}",
        reply_markup=reply_markup
    )

# BUTTON MENU HANDLER
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "📚 Notes":
        await update.message.reply_text("📚 Biology Notes Coming Soon")

    elif text == "🧠 Test":
        await send_quiz(update, context)

    elif text == "💎 Premium":
        await update.message.reply_text("💎 Premium access soon")

    elif text == "❓ Help":
        await update.message.reply_text("Use buttons below 👇")

# QUIZ BUTTON CHECK
async def quiz_button(update, context):

    query = update.callback_query
    await query.answer()

    data = query.data.split("|")

    q_index = int(data[0])
    selected = data[1]

    correct = quiz_data[q_index]["answer"]

    if selected == correct:
        await query.message.reply_text("✅ Correct Answer")

    else:
        await query.message.reply_text(
            f"❌ Wrong Answer\nCorrect Answer: {correct}"
        )

   await query.message.reply_text("🏁 Quiz Finished")

# APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)

app.add_handler(CallbackQueryHandler(quiz_button))

print("Bot Running...")

app.run_polling(stop_signals=None)
