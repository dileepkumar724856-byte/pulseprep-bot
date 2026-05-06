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

TOKEN = os.getenv("TOKEN")

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

# QUIZ POLL
async def send_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):

    question = "Mendel's law of independent assortment is applicable for:"

    options = [
        "All genes in all organisms",
        "All genes of pea plant only",
        "All non linked genes only",
        "All linked genes only"
    ]

    correct_option = 2

    await update.message.reply_poll(
        question=question,
        options=options,
        type="quiz",
        correct_option_id=correct_option,
        explanation="Independent assortment works for non-linked genes."
    )

# HANDLE BUTTONS
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

        await send_poll(update, context)

    elif text == "💎 Premium":

        await update.message.reply_text(
            "💎 Premium coming soon"
        )

    elif text == "❓ Help":

        await update.message.reply_text(
            "Use menu buttons below 👇"
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
