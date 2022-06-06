from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from configs import Config

@Client.on_message(filters.private, group=-1)
async def fsub(Client, Message):
    id = Message.from_user.id
    if Config.UPDATES_CHANNEL:
        try:
            await Client.get_chat_member(Config.UPDATES_CHANNEL, id)
        except UserNotParticipant:
            await Client.send_message(
                id,
                "Join My Updates Channel To Use Me!",
                reply_to_message_id = Message.message_id,
                reply_markup = InlineKeyboardMarkup(
                    [ 
                        [ 
                            InlineKeyboardButton("Join", url=f"https://t.me/{Config.UPDATES_CHANNEL}") 
                        ]   
                    ]
                )
            )
