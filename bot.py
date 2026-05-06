from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN =os .getenv("TOKEN")

async def set_menu(app):
    commands = [
        BotCommand("start", "🚀 Start"),
        BotCommand("notes", "📚 Notes"),
        BotCommand("quiz", "🧠 Quiz"),
    ]
    await app.bot.set_my_commands(commands)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome 🚀")

app = ApplicationBuilder().token(TOKEN).build()

app.post_init = set_menu
