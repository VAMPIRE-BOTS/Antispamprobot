from pyrogram import Client, filters
from config import OWNER_ID

from app.modules.broadcast import USERS

GROUPS = set()

@Client.on_message(filters.group)
async def save_groups(client, message):

    GROUPS.add(message.chat.id)

@Client.on_message(
    filters.command("stats")
    & filters.user(OWNER_ID)
)
async def stats_handler(client, message):

    await message.reply_text(
        f"📊 Bot Statistics\n\n"

        f"👤 Users: {len(USERS)}\n"
        f"👥 Groups: {len(GROUPS)}"
    )
