async def notes_hub(update):

    text = """
📚 NOTES HUB

⚡ Physics Notes
🧬 Biology Notes
🧪 Chemistry Notes

🔥 PYQ Notes
🧠 Formula Sheets
📘 Short Notes

🚀 More Notes Coming Soon
"""

    await update.message.reply_text(text)
