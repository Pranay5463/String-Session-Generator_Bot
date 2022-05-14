from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from Config import UPDATES_CHANNEL

@Client.on_message(filters.private)
async def fsub(Client, Message):
    id = Message.from_user.id
    if UPDATES_CHANNEL:
        try:
            await Client.get_chat_member(Config.UPDATES_CHANNEL, id)
        except UserNotParticipant:
            await Client.send_message(
                id,
                "Join",
                reply_to_message_id = Message.message_id,
                reply_markup = InlineKeyboardMarkup(
                    [ 
                        [ 
                            InlineKeyboardButton("Join", url=f"https://t.me/{Config.UPDATES_CHANNEL}") 
                        ]   
                    ]
                )
            )
