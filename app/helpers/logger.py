from config import LOG_GROUP_ID

async def log_new_user(client, user):

    try:

        await client.send_message(
            LOG_GROUP_ID,
            (
                f"🆕 New User Started Bot\n\n"

                f"👤 Name: {user.mention}\n"
                f"🆔 ID: `{user.id}`\n"
                f"📛 Username: @{user.username}"
            )
        )

    except:
        pass


async def log_new_group(client, chat, adder):

    try:

        await client.send_message(
            LOG_GROUP_ID,
            (
                f"➕ Bot Added To New Group\n\n"

                f"🏷 Group Name: {chat.title}\n"
                f"🆔 Group ID: `{chat.id}`\n\n"

                f"👤 Added By: {adder.mention}\n"
                f"📛 Username: @{adder.username}"
            )
        )

    except:
        pass
