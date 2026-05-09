from pyrogram.errors import UserNotParticipant

# यहाँ पर आपका चैनल का यूजरनेम सीधे सेट कर दिया गया है
MUST_JOIN = "VAMPIREUPDATES"

async def is_subscribed(client, user_id):
    try:
        await client.get_chat_member(MUST_JOIN, user_id)
        return True
        
    except UserNotParticipant:
        return False
        
    except:
        return True
