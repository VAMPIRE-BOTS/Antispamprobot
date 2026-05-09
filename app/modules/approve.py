from pyrogram import Client, filters
from config import OWNER_ID

from app.modules.protection import APPROVED_USERS

@Client.on_message(
    filters.command("approve")
    & filters.user(OWNER_ID)
)
async def approve_user(client, message):

    if not message.reply_to_message:

        return await message.reply_text(
            "Reply to a user."
        )

    user_id = message.reply_to_message.from_user.id

    APPROVED_USERS.add(user_id)

    await message.reply_text(
        f"✅ Approved User: {user_id}"
    )
