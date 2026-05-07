import random
from questions.leader_test import leader_test

from questions.units_questions import units_questions

async def send_quiz(update):
    async def send_leader_test(update):

    import random

    q = random.choice(leader_test)

    await update.message.reply_poll(
        question=f"🔥 {q['question']}",
        options=q["options"],
        type="quiz",
        correct_option_id=q["answer"],
        explanation=q["explanation"],
        is_anonymous=False
    )

    q = random.choice(units_questions)

    await update.message.reply_poll(
        question=f"⚡ {q['question']}\n\n📘 {q['year']}",
        options=q["options"],
        type="quiz",
        correct_option_id=q["answer"],
        explanation=f"✅ {q['explanation']}",
        is_anonymous=False
    )
