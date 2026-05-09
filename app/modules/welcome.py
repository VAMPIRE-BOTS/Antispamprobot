from pyrogram import Client, filters

from config import PHOTO_URL

from app.helpers.buttons import START_BUTTONS
from app.helpers.logger import log_new_group

@Client.on_message(filters.new_chat_members)
async def welcome_members(client, message):

    for member in message.new_chat_members:

        if member.id == (await client.get_me()).id:

            if message.from_user:

                await log_new_group(
                    client,
                    message.chat,
                    message.from_user
                )

        await message.reply_photo(
            photo=PHOTO_URL,
            caption=(
                f"✨ Welcome {member.mention}\n\n"

                f"🛡️ Security Shield Activated\n\n"

                f"This group is protected by "
                f"ANTI ABUSE PRO BOT.\n\n"

                f"🚫 Abuse Not Allowed\n"
                f"🚫 NSFW Not Allowed\n"
                f"🚫 Spam Not Allowed\n\n"

                f"⚡ Enjoy your stay."
            ),
            reply_markup=START_BUTTONS
        )
