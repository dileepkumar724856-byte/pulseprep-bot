from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
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

TOKEN = os.getenv("TOKEN")

# MENU BUTTONS
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
# BUTTON HANDLER
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Notes":
        await update.message.reply_text("📚 Biology Notes Coming Soon")

    elif text == "🧠 Test":
        await update.message.reply_text("🧠 Daily Test Coming Soon")

    elif text == "💎 Premium":
        await update.message.reply_text("💎 Premium access soon")

    elif text == "❓ Help":
        await update.message.reply_text("Use buttons below 👇")

# APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

# MENU BUTTONS
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
        reply_markup=reply_markuasync 
# BUTTON HANDLER
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Notes":
        await update.message.reply_text("📚 Biology Notes Coming Soon")

    elif text == "🧠 Test":
        await update.message.reply_text("🧠 Daily Test Coming Soon")

    elif text == "💎 Premium":
        await update.message.reply_text("💎 Premium access soon")

    elif text == "❓ Help":
        await update.message.reply_text("Use buttons below 👇")

# APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

# MENU BUTTONS
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

# BUTTON HANDLER
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Notes":
        await update.message.reply_text("📚 Biology Notes Coming Soon")

    elif text == "🧠 Test":
        await update.message.reply_text("🧠 Daily Test Coming Soon")

    elif text == "💎 Premium":
        await update.message.reply_text("💎 Premium access soon")

    elif text == "❓ Help":
        await update.message.reply_text("Use buttons below 👇")

# APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
