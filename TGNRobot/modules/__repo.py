import os
from pyrogram import Client, filters
from pyrogram.types import *

from FlorinaRobot.conf import get_str_key
from FlorinaRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/cab6825dea9263d347831.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [Faraday](t.me/faraday789) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @The_Godfather_Network «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ ʀᴇᴘᴏꜱɪᴛᴏʀʏ🔥", url=f"https://github.com/KUNAL12459/Florina-Robot"),
        InlineKeyboardButton(" ᴊᴏɪɴ 💫", url=f"https://t.me/Superior_Bots"),
      ],[
        InlineKeyboardButton("ᴛɢɴ ᴏᴡɴᴇʀ ❣️", url="https://t.me/faraday789"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/florina_support"),
      ],[
        InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ☑️", url="https://t.me/florina_channel"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ➡️", url="https://t.me/faraday789"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
