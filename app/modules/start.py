from pyrogram import Client, filters
from config import PHOTO_URL
from app.helpers.buttons import *
from app.helpers.checker import is_subscribed
from app.helpers.logger import log_new_user

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):

    if not await is_subscribed(
        client,
        message.from_user.id
    ):

        return await message.reply_photo(
            photo=PHOTO_URL,
            caption=(
                "⚠️ Access Denied\n\n"
                "Join our updates channel first."
            ),
            reply_markup=FORCE_JOIN_BUTTONS
        )

    await log_new_user(client, message.from_user)

    await message.reply_photo(
        photo=PHOTO_URL,
        caption=(
            f"✨ Hello {message.from_user.mention}\n\n"

            f"🛡️ Welcome To ANTI ABUSE PRO BOT X\n\n"

            f"Advanced Telegram Protection System.\n\n"

            f"✅ Anti Abuse\n"
            f"✅ Anti Toxic Words\n"
            f"✅ Anti NSFW\n"
            f"✅ Anti Spam\n"
            f"✅ Auto Warnings\n"
            f"✅ Auto Mute\n\n"

            f"⚡ Fast • Smart • Powerful"
        ),
        reply_markup=START_BUTTONS
    )
