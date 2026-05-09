from pyrogram import Client
from config import *

plugins = dict(root="app.modules")

app = Client(
    "VampGuardX",
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins
)

print("🛡️ VampGuard X Started Successfully ✅")

app.run()
