from pyrogram import Client, filters
from pyrogram.types import Message

from app.helpers.detector import detect_abuse

APPROVED_USERS = set()

WARNS = {}

@Client.on_message(filters.group & ~filters.service)
async def protection_engine(client, message: Message):

    if not message.from_user:
        return

    user_id = message.from_user.id

    if user_id in APPROVED_USERS:
        return

    try:

        member = await client.get_chat_member(
            message.chat.id,
            user_id
        )

        if member.status in (
            "administrator",
            "creator"
        ):
            return

    except:
        pass

    content = message.text or message.caption or ""

    if detect_abuse(content):

        try:
            await message.delete()
        except:
            pass

        WARNS[user_id] = WARNS.get(user_id, 0) + 1

        warns = WARNS[user_id]

        await message.reply_text(
            f"⚠️ Warning {warns}/3\n"
            f"Abusive language detected."
        )

        if warns >= 3:

            try:

                await client.restrict_chat_member(
                    message.chat.id,
                    user_id,
                    permissions={}
                )

                await message.reply_text(
                    "🔇 User muted automatically."
                )

            except:
                pass

    if (
        message.sticker
        or message.animation
        or message.video_note
    ):

        try:
            await message.delete()
        except:
            pass
