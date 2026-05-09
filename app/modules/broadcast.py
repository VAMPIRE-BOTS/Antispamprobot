from pyrogram import Client, filters
from config import OWNER_ID

USERS = set()

@Client.on_message(filters.private)
async def save_users(client, message):

    USERS.add(message.from_user.id)

@Client.on_message(
    filters.command("broadcast")
    & filters.user(OWNER_ID)
)
async def broadcast_handler(client, message):

    if not message.reply_to_message:

        return await message.reply_text(
            "Reply to message for broadcast."
        )

    sent = 0
    failed = 0

    for user_id in USERS:

        try:

            await message.reply_to_message.copy(user_id)

            sent += 1

        except:

            failed += 1

    await message.reply_text(
        f"✅ Broadcast Completed\n\n"
        f"📤 Sent: {sent}\n"
        f"❌ Failed: {failed}"
    )
