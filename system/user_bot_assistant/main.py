#    Copyright (C) 2021 KeinShin

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>

import asyncio
import heroku3
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from system.Config import *
from system import OWNER, bot, app, ASSISTANT_HELP
from pyrogram.types import (   InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup



)

from pyrogram import *
from math import ceil

from system.Config  import Variable as Var

import coffeehouse

from coffeehouse.lydia import LydiaAI
import os

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
from PIL import Image, ImageDraw, ImageFont

how = []
total_cmds = []

LYDIA_AP = {}
SESSION_ID = {}
TEMP_DIR = "./system/temp_files"
if not os.path.isdir(TEMP_DIR):
        os.makedirs(TEMP_DIR)
import os
temp = TEMP_DIR
CHAT_BOT = os.environ.get("CHAT_BOT", None)
GROUP_ASSITANT = os.environ.get("GROUP_ASSITANT", None)

ASISTANT_CMD_ROWS = os.environ.get("GROUP_ASSITANT", None)
if ASISTANT_CMD_ROWS is None:
   ASISTANT_CMD_ROWS = 7
else:
   number_of_rows_in_commands = ASISTANT_CMD_ROWS



plugs = []
tgbot = bot



ASISTANT_CMD_COLUMNS = os.environ.get("GROUP_ASSITANT", None)
if ASISTANT_CMD_COLUMNS is None:
   ASISTANT_CMD_COLUMNS = 5
else:
   number_of_columns_in_commands = ASISTANT_CMD_COLUMNS


   
ASSISTANT_PIC = os.environ.get("ASSISTANT_PIC", None)
if ASSISTANT_PIC is None:
    PIC = "https://telegra.ph/file/4e83650cf1e3e8c31c51b.mp4"
else:
    PIC = ASSISTANT_PIC

CHAT_BOT_API = os.environ.get("CHAT_BOT_API", None)
if CHAT_BOT_API is None:
    C_API = "e20daaf7e63f680cb1ba4d004a85981873f75ba260f2253e57ded815add3c2bab3388c085c8ad5469faf798bd1bfc2000edc6876566ae584d7db07623a9b7328"
else:
    C_API = CHAT_BOT_API


    lydia_ley = C_API
    client = coffeehouse.API(lydia_ley)
    Lydia = LydiaAI(client)

ownesr = str(Variable.OWNER_NAME)

@bot.on_message(filters.command(["start"]) & filters.incoming)
async def send_welcome(client, message):
      pis = PIC
      co = await app.get_me()

      
      if message.chat.id == co.id:
            txt = "**Hi! I'm Your Assistant Master\n\nAny One Can Contact You Via Me\n\nI'll Get users messages to you**\n\n[Feat. by ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ ᴜsᴇʀʙᴏᴛ](https://github.com/KeinShin/Black-Lightning)"
     
            mrkup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="❤️Users❤️", callback_data="users")],
                [InlineKeyboardButton(text="Chat Bot😸", callback_data="chat_bot")],
                [InlineKeyboardButton(text="Help!", url="https://t.me/black_lightning_channel")]
            ]
            ) 
 #    pis = pic()
            await bot.send_document(
                 message.chat.id,
                 document=PIC,
                 caption=txt,
                 reply_markup=mrkup,
                 force_document=False)
      else:
             mkp =InlineKeyboardMarkup([
                 [InlineKeyboardButton(text="Commands", callback_data="commands")],
                [InlineKeyboardButton(text="Help!", url="https://t.me/black_lightning_channel")]
                ]
                )
             user = await app.get_users(int(message.chat.id))
             owner = str(Variable.OWNER_NAME)
             kok = f"**Hello {user.first_name }!\n\n Thanks for Contacting {owner}\n\nI'm assisting  {owner} Kindly Leave Your Message**\n\nFeatured By [ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ ᴜsᴇʀʙᴏᴛ](https://github.com/KeinShin/Black-Lightning)"
             await bot.send_message(
                 message.chat.id,
                 PIC,
                 kok,
                 reply_markup=mkp)
           


                            # @tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))

import re

USER = OWNER


# @bot.on_callback_query(filters.regex(pattern="users"))


# async def d(client ,message):
#     with io.BytesIO(str.encode(get_ids())) as out_file:
#         out_file.name = "cmd_list.txt"
#     await bot.send_document(message.chat.id, document=out_file)


    

@bot.on_message(filters.command(['ask']) & filters.incoming)

async def ask(client, message):
    user = await app.get_users(int(message.chat.id))
    if user.id == app.get_me().id:
     username=Var.OWNER_NAME
     await tgbot.send_message(f"Hi Dear,\n\nNow you can ask your question i'll send it to {username}")













@bot.on_message(filters.command("^", ["Hi"]) & filters.incoming)
async def send_welcome(client, message):
      if CHAT_BOT == 'ENABLE':
          return
      ssendr = message.sender_id
      ko=await bot.get_me()
      
      if ssendr == ko.id :
       await tgbot.send_message(message.chat.id, "**Hi! Master If You Want That I Talk!**\n\n**Kindly Enable Chatbot**\n\n**You Can Chat With Me :)**")
      
      else:
       await tgbot.send_message(message.chat.id, "**Hi! How Can I Help?**\n\n**Kindly Leave The Message**\n\n**You Can ask my master by doin !ask :)**")



# @tgbot.on(messages.NewMessage(pattern="^Help"))
# async def send_welcome(event):
#     if CHAT_BOT == 'ENABLE':
#      return
#     user =OWNER # U s k a B a s  c h a l e  t o  s a r a d a r i y a  p i i  j a y e, a a e k h u d a  t u  b o l d e   t e r e   b a d l o  k o 
    
#     sendr = event.sender_id
#     from userbot import bot
    
#     owner=await bot.get_me()
      
#     if sendr == owner.id :
#        await tgbot.send_message(event.chat.id, "**Hi! Master If You Want That I Talk!**\n\n**Kindly Enable Chatbot Then, You Can Chat With Me :)**")
#     else:
#        await tgbot.send_message(event.chat.id, f"**Kindly Leave The Message**\n\n**I Will Pass It To {user}**")


