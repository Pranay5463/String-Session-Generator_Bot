from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʟʟᴏ {}

ᴡᴇʟʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ. 

ɪ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴡɪᴛʜ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ. 

ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ: [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/telugucoders) 
"""

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇ ғʀᴏᴍ ʜᴇʀᴇ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(" Give a Star ⭐", url="https://github.com/Pranay5463/String-Session-Generator_Bot")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton(" Get Help ↗️", url="https://t.me/+9SetglBX6YY0OWRh")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - To display current Message
/start - Start the Bot
/generate - Generate String Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by @NotrealPranay

Source Code : [Click Here](https://github.com/Pranay5463/String-Session-Generator_Bot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @NotrealPranay
    """
