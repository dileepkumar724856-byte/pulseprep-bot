async def leaderboard(update, user_xp):

    if not user_xp:

        await update.message.reply_text(
            "🏆 No Students Yet"
        )

        return

    sorted_users = sorted(
        user_xp.items(),
        key=lambda x: x[1],
        reverse=True
    )

    text = "🏆 AIR LEADERBOARD 🏆\n\n"

    rank = 1

    for user_id, xp in sorted_users[:5]:

        text += f"{rank}. User {user_id} → {xp} XP\n"

        rank += 1

    await update.message.reply_text(text)
