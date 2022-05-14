from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from .database.mongo import insert, find_one

@Client.on_message(filters.private & filters.incoming & filters.command("about"))
async def _about(bot, msg):
	id = msg.from_user.id
	ok = find_one(id)
	if ok:
		await bot.send_message(
			msg.chat.id,
			"**Here's how to use me **\n" + Data.ABOUT,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		)
	else:
		insert(id)
		await msg.reply_text(
			text=Data.ABOUT, 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		) 

@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(bot, msg):
	id = msg.from_user.id
	ok = find_one(id)
	if ok:
		await bot.send_message(
			msg.chat.id,
			"**Here's how to use me **\n" + Data.HELP,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		)
	else:
		insert(id)
		await msg.reply_text(
			text=Data.HELP, 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		) 

@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def _start(bot, msg):
	id = msg.from_user.id
	ok = find_one(id)
	if ok:
		await bot.send_message(
			msg.chat.id,
			"**Here's how to use me **\n" + Data.START,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		)
	else:
		insert(id)
		await msg.reply_text(
			text=Data.START, 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		) 
