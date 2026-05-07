import random

from questions.units_questions import units_questions

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
