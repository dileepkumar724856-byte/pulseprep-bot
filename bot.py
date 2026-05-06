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

# USER SCORES
user_data = {}

# MENU BUTTONS
MENU = [
    ["📚 Notes", "🧠 Test"],
    ["💎 Premium", "❓ Help"]
]

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🚀 Welcome to PulsePrep NEET Bot",
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# SEND QUIZ
async def send_quiz(message, context, q_index=0):

    question = quiz_data[q_index]

    keyboard = []

    for option in question["options"]:

        keyboard.append([
            InlineKeyboardButton(
                option,
                callback_data=f"{q_index}|{option}"
            )
        ])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await message.reply_text(
        f"🧠 {question['question']}",
        reply_markup=reply_markup
    )

# HANDLE MENU BUTTONS
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

# QUIZ BUTTON HANDLER
async def quiz_button(update, context):

    query = update.callback_query

    await query.answer()

    user_id = query.from_user.id

    if user_id not in user_data:

        user_data[user_id] = 0

    data = query.data.split("|")

    q_index = int(data[0])

    selected = data[1]

    correct = quiz_data[q_index]["answer"]

    # CHECK ANSWER
    if selected == correct:

        user_data[user_id] += 1

        await query.message.reply_text(
            "✅ Correct Answer"
        )

    else:

        await query.message.reply_text(
            f"❌ Wrong Answer\n✅ Correct: {correct}"
        )

    # NEXT QUESTION
    next_q = q_index + 1

    if next_q < len(quiz_data):

        await send_quiz(
            query.message,
            context,
            next_q
        )

    else:

        score = user_data[user_id]

        await query.message.reply_text(
            f"🏁 Quiz Finished\n🎯 Score: {score}/{len(quiz_data)}"
        )

        user_data[user_id] = 0

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
