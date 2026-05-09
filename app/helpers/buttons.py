from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *

START_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "➕ Add Me To Your Group",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
        )
    ],
    [
        InlineKeyboardButton(
            "📢 Updates",
            url=f"https://t.me/{MUST_JOIN}"
        ),

        InlineKeyboardButton(
            "🛠 Help",
            callback_data="help_menu"
        )
    ],
    [
        InlineKeyboardButton(
            "👑 Owner",
            user_id=OWNER_ID
        )
    ]
])

HELP_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "🔙 Back",
            callback_data="back_start"
        )
    ]
])

FORCE_JOIN_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "📢 Join Updates Channel",
            url=f"https://t.me/{MUST_JOIN}"
        )
    ],
    [
        InlineKeyboardButton(
            "✅ Verify Join",
            callback_data="check_join"
        )
    ]
])
