from pyrogram import Client
from config import *

plugins = {"root": "app.modules"}

app = Client(
    name="VampGuardX",
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins,
    workers=50
)

print("🛡️ VampGuard X Started Successfully ✅")

app.run()
