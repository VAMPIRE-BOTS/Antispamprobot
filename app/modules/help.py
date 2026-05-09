from pyrogram import Client
from pyrogram.types import CallbackQuery

from app.helpers.buttons import *

@Client.on_callback_query()
async def callbacks(client, query: CallbackQuery):

    if query.data == "help_menu":

        await query.message.edit_caption(
            caption=(
                "🛠 ANTI ABUSE PRO BOT X Help Menu\n\n"

                "📌 Commands\n\n"

                "/start → Start the bot\n"
                "/approve → Approve user\n"
                "/unapprove → Remove approved user\n"
                "/broadcast → Broadcast message\n"
                "/stats → Bot statistics\n\n"

                "🛡 Features\n\n"

                "✅ Anti Abuse\n"
                "✅ Anti NSFW\n"
                "✅ Anti Toxic Words\n"
                "✅ Auto Delete\n"
                "✅ Auto Warn\n"
                "✅ Auto Mute"
            ),
            reply_markup=HELP_BUTTONS
        )

    elif query.data == "back_start":

        await query.message.edit_caption(
            caption=(
                f"✨ Hello {query.from_user.mention}\n\n"
                f"🛡️ Welcome Back To ANTI ABUSE PRO BOT"
            ),
            reply_markup=START_BUTTONS
        )

    elif query.data == "check_join":

        await query.answer(
            "✅ Join Verified",
            show_alert=True
        )
