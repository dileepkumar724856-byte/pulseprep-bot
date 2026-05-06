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

# MAIN MENU
MENU = [
    ["📚 Notes", "🎲 Quiz"],
    ["💎 Premium", "❓ Help"]
]

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
━━━━━━━━━━━━━━
🚀 PULSEPREP NOTES BOT
━━━━━━━━━━━━━━

📚 Chapter Notes
🎲 Daily Quiz
💎 Premium Access

Choose Option 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

# NOTES MENU
async def notes_menu(update):

    keyboard = [

        [
            InlineKeyboardButton(
                "🧬 Biology",
                callback_data="bio"
            )
        ],

        [
            InlineKeyboardButton(
                "⚡ Physics",
                callback_data="physics"
            )
        ],

        [
            InlineKeyboardButton(
                "🧪 Chemistry",
                callback_data="chem"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📚 Select Subject",
        reply_markup=reply_markup
    )

# BIOLOGY CHAPTERS
async def biology_menu(query):

    keyboard = [

        [
            InlineKeyboardButton(
                "🧬 Cell",
                callback_data="cell"
            )
        ],

        [
            InlineKeyboardButton(
                "🧬 Genetics",
                callback_data="genetics"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text(
        "🧬 Biology Chapters",
        reply_markup=reply_markup
    )

# PHYSICS CHAPTERS
async def physics_menu(query):

    keyboard = [

        [
            InlineKeyboardButton(
                "⚡ Current Electricity",
                callback_data="current"
            )
        ],

        [
            InlineKeyboardButton(
                "⚡ Ray Optics",
                callback_data="optics"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text(
        "⚡ Physics Chapters",
        reply_markup=reply_markup
    )

# CHEMISTRY CHAPTERS
async def chemistry_menu(query):

    keyboard = [

        [
            InlineKeyboardButton(
                "🧪 Chemical Bonding",
                callback_data="bonding"
            )
        ],

        [
            InlineKeyboardButton(
                "🧪 Thermodynamics",
                callback_data="thermo"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text(
        "🧪 Chemistry Chapters",
        reply_markup=reply_markup
    )

# HANDLE MAIN MENU
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    if text == "📚 Notes":

        await notes_menu(update)

    elif text == "🎲 Quiz":

        await update.message.reply_poll(
            question="SI unit of force?",
            options=[
                "Newton",
                "Joule",
                "Watt",
                "Pascal"
            ],
            type="quiz",
            correct_option_id=0,
            explanation="SI unit of force is Newton."
        )

    elif text == "💎 Premium":

        await update.message.reply_text(
            "💎 Premium Coming Soon"
        )

    elif text == "❓ Help":

        await update.message.reply_text(
            "Use Buttons Below 👇"
        )

# HANDLE INLINE BUTTONS
async def button_click(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data

    # SUBJECT MENUS
    if data == "bio":

        await biology_menu(query)

    elif data == "physics":

        await physics_menu(query)

    elif data == "chem":

        await chemistry_menu(query)

    # PDF SEND
    elif data == "cell":

        await query.message.reply_document(
            document=open("biology.pdf", "rb"),
            caption="🧬 Cell Notes"
        )

    elif data == "genetics":

        await query.message.reply_document(
            document=open("biology.pdf", "rb"),
            caption="🧬 Genetics Notes"
        )

    elif data == "current":

        await query.message.reply_document(
            document=open("physics.pdf", "rb"),
            caption="⚡ Current Electricity Notes"
        )

    elif data == "optics":

        await query.message.reply_document(
            document=open("physics.pdf", "rb"),
            caption="⚡ Ray Optics Notes"
        )

    elif data == "bonding":

        await query.message.reply_document(
            document=open("chemistry.pdf", "rb"),
            caption="🧪 Chemical Bonding Notes"
        )

    elif data == "thermo":

        await query.message.reply_document(
            document=open("chemistry.pdf", "rb"),
            caption="🧪 Thermodynamics Notes"
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
    CallbackQueryHandler(button_click)
)

print("Bot Running...")

# RUN BOT
app.run_polling()
