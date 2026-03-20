from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import LOGGER_ID as LOG_GROUP_ID
from Oneforall import app
from Oneforall.utils.database import get_assistant

PHOTO = "https://graph.org/file/d22cec7c75e26f36edff7-0ce8cae0037d4aa0aa.jpg"


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat

        for member in message.new_chat_members:
            if member.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = chat.username if chat.username else "Private Group"

                msg = (
                    f"New Group Added\n\n"
                    f"Name: {chat.title}\n"
                    f"ID: {chat.id}\n"
                    f"Username: @{username}\n"
                    f"Members: {count}\n"
                    f"Added by: {message.from_user.mention}"
                )

                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=PHOTO,
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Added By",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )

                if chat.username:
                    await userbot.join_chat(chat.username)

    except Exception as e:
        print(f"Error: {e}")
