from pyrogram import Client, filters
from pyrogram.types import Message

from config import PHOTO_URL
from app.helpers.buttons import START_BUTTONS, FORCE_JOIN_BUTTONS
from app.helpers.checker import is_subscribed
from app.helpers.logger import log_new_user


@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):

    try:
        join = await is_subscribed(
            client,
            message.from_user.id
        )

        if not join:
            return await message.reply_photo(
                photo=PHOTO_URL,
                caption=(
                    "⚠️ Access Denied!\n\n"
                    "Please join our updates channel first "
                    "to use this bot."
                ),
                reply_markup=FORCE_JOIN_BUTTONS
            )

        await log_new_user(client, message.from_user)

        await message.reply_photo(
            photo=PHOTO_URL,
            caption=(
                f"✨ Hello {message.from_user.mention}\n\n"

                f"🛡️ Welcome To ANTI SPAM PRO BOT\n\n"

                f"Advanced Telegram Protection System.\n\n"

                f"✅ Anti Abuse Protection\n"
                f"✅ Toxic Words Detection\n"
                f"✅ NSFW Content Blocker\n"
                f"✅ Auto Spam Delete\n"
                f"✅ Auto Warning System\n"
                f"✅ Auto Mute System\n"
                f"✅ Group Security Engine\n\n"

                f"⚡ Fast • Smart • Powerful"
            ),
            reply_markup=START_BUTTONS
        )

    except Exception as e:
        print(f"START ERROR : {e}")
