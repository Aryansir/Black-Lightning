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
from system.Config import Variable
from system import OWNER, bot, app, ASSISTANT_HELP
from pyrogram.types import (   InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup



)

from pyrogram import *
from math import ceil


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
    PIC = "https://telegra.ph/file/b5afd12c58bfca1f1d47b.jpg"
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

      
      if message.chat_id == co.id:
            txt = "**Hi! I'm Your Assistant Master\n\nAny One Can Contact You Via Me\n\nI'll Get users messages to you**\n\n[Feat. by ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ ᴜsᴇʀʙᴏᴛ](https://github.com/KeinShin/Black-Lightning)"
     
            mrkup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="❤️Users❤️", callback_data="users")],
                [InlineKeyboardButton(text="Chat Bot😸", callback_data="chat_bot")],
                [InlineKeyboardButton(text="Commands", callback_data="commands")],
                [InlineKeyboardButton(text="Help!", url="@lightning_support_grup")]
            ]
            ) 
 #    pis = pic()
            await bot.send_message(
                 message.chat_id,
                 PIC,
                 txt,
                 reply_markup=mrkup)
      else:
             mkp =InlineKeyboardMarkup([
                 [InlineKeyboardButton(text="Commands", callback_data="commands")],
                [InlineKeyboardButton(text="Help!", url="@lightning_support_grup")]
                ]
                )
             user = await app.get_users(int(message.chat_id))
             owner = str(Variable.OWNER_NAME)
             kok = f"**Hello {user.first_name }!\n\n Thanks for Contacting {owner}\n\nI'm assisting  {owner} Kindly Leave Your Message**\n\nFeatured By [ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ ᴜsᴇʀʙᴏᴛ](https://github.com/KeinShin/Black-Lightning)"
             await bot.send_message(
                 message.chat_id,
                 PIC,
                 kok,
                 reply_markup=mkp)
           


                            # @tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))

import re

USER = OWNER

@bot.on_inline_query()
async def help(client, inline_query):
    fucking_sucking = await bot.get_me()
    text = inline_query.query
    if text == "Assistant Menu":

        content = InputTextMessageContent("**Black Lightning ASSISTANT Help Menu for User** [{}]({})".format(USER[1:],  fucking_sucking.id))
        await inline_query.answer(result=[
        InlineQueryResultArticle(
                    
                    title="Help Menu",
                    input_message_content=content,
                    description="Help for command",
                    reply_markup=InlineKeyboardMarkup(assitant_help(0, ASSISTANT_HELP, "help")),
        )],
        cache_time=0)


@bot.on_message(filters.command(["Commands"]) & filters.incoming)
async def command(client ,event):
    for i in ASSISTANT_HELP:
        if i.startswith('_'):
            return
        plugs.append(i)
    des = sorted(plugs)
    
    buttons = assitant_help(0, ASSISTANT_HELP, 'help')
    if des in ASSISTANT_HELP:

     await event.edit_message_reply_markup(reply_markup =buttons)

@bot.on_callback_query(filters.regex(pattern="_total_cmds_(.*)"))

async def lightning_pugins_query_hndlr(client ,event):
    command = ASSISTANT_HELP['Command']
    cmd = event.matches[0].group(1)
    type = ASSISTANT_HELP[f"{cmd}'s Type"]
    try:
    
     if cmd in ASSISTANT_HELP:
        assistant_help_strin = f"**✡ Type : {type} ✡**"
        assistant_help_strin  += f"**🔺 COMMAND 🔺 :** `{cmd}` \n\n{command}"
        
        assistant_buttons = assistant_help_strin 
        assistant_buttons += "\n\n**In Case Any Problem @lightning_support_grup**".format(cmd)
        await event.edit(assistant_buttons)
    
    except KeyError:
        await event.answer("The command isn't displayable", cache_time=0, alert=True)


@bot.on_callback_query(filters.regex(pattern="help_preve\((.+?)\)"))

async def lightning_pugins_query_hndlr(client, lightning):
    
        lightning_page = int(lightning.matches[0].group(1))
        buttons = assitant_help(
            lightning_page - 1, ASSISTANT_HELP, "help"  # pylint:disable=E0602
        )
        await lightning.edit_message_reply_markup(reply_markup=buttons)

import io
from system.sqls.bot_sql import *

@bot.on_callback_query(filters.regex(pattern="users"))


async def d(client ,message):
    with io.BytesIO(str.encode(get_ids())) as out_file:
        out_file.name = "cmd_list.txt"
    await bot.send_document(message.chat_id, document=out_file)

@bot.on_callback_query(filters.regex(pattern="help_nexte\((.+?)\)"))
  
async def ass_pugins_query_hndlr(client, lightning):
        await lightning.delete()
        lightning_page = int(lightning.matches[0].group(1))
        
        buttons = assitant_help(
            lightning_page + 1, ASSISTANT_HELP, "help"  # pylint:disable=E0602
        )
        await lightning.edit_message_reply_markup(reply_markup=buttons)



#    Copyright (C) 2020 Telebot

def assitant_help(b_lac_krish, lightning_plugs, lightning_lol):

 total_cmds = []
 for p in lightning_plugs:
     if not p.startswith("_"):
         total_cmds.append(p)
 total_cmds = sorted(total_cmds)
 plugins = [
     InlineKeyboardButton(
         "{}".format( x), callback_data="_total_cmds_{}".format(x)
     )
     for x in total_cmds
 ]
 pairs = list(zip(plugins[::number_of_columns_in_commands], plugins[1::number_of_columns_in_commands]))
 if len(plugins) % number_of_columns_in_commands == 1:
     pairs.append((plugins[-1],))
 max_fix = ceil(len(pairs) / number_of_rows_in_commands)
 total_cmds_pages = b_lac_krish % max_fix
 
 if len(pairs) > number_of_rows_in_commands:
   

     pairs = pairs[
         total_cmds_pages * number_of_rows_in_commands : number_of_rows_in_commands * (total_cmds_pages + 1)
     ] + [
         (
             InlineKeyboardButton(
                 "Previous", callback_data="{}_prev({})".format(lightning_lol, total_cmds_pages)
             ),
            
            InlineKeyboardButton(
                 "Next", callback_data="{}_next({})".format(lightning_lol, total_cmds_pages)
             ),
             
         )
     ]
 else:
   pairs = pairs[
       total_cmds_pages * ASISTANT_CMD_ROWS : ASISTANT_CMD_ROWS * (total_cmds_pages + 1)
   
   ]

 return pairs





@bot.on_message(filters.command("!", ["ask"]) & filters.incoming)

async def ask(client, message):
    user = await app.get_users(int(message.chat_id))
    if user.id == app.me.id:
     username=Var.OWNER_NAME
     await tgbot.send_message(f"Hi Dear,\n\nNow you can ask your question i'll send it to {username}")






@bot.on_callback_query(filters.regex(pattern="chat_bot"))
async def commands(client, message):

   co = await app.get_users(int(message.chat_id))

   if CHAT_BOT == "ENABLE":
    tgbot.send_message(message.chat_id,  
    "Chat Bot Already Enabled",)
    buttons=InlineKeyboardButton(text="Deactivate", callback_data="lol_nvm")

   else:
    kok = f"**What Chat Bot Does?**\n\n**Answer - Chatbot Will Activate Artificial intelligence Of Your Bot\nIn Short Bot Will Chat With The User Like a Human**"
    await tgbot.send_message(message.chat_id,  
    kok)
    buttons=InlineKeyboardButton(text="Deactivate", callback_data="activate")

@bot.on_callback_query(filters.regex(pattern="activate"))
async def chatboot(client, message):
    app= Heroku.app(Var.HEROKU_APP_NAME)
    var=app.config()
    var[CHAT_BOT] = 'ENABLE'
    me = await app.get_me()
    await tgbot.send_message(message.chat_id, "Chat Bot Activated")
    apps = Heroku.app(Var.HEROKU_APP_NAME)

    kek = await message.sender_id
    id = await bot.get_users(int(message.chat_id))
    session = Lydia.create_session()
    session_id = session.id
    LYDIA_AP.update({str(message.chat_id) + " " + str(id.from_id): session})
    SESSION_ID.update(
            {str(message.chat_id) + " " + str(id.from_id): session_id}
        )
@bot.on_callback_query(filters.regex(pattern="lol_nvm"))
async def chatboot(client, message):
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    heroku_var[CHAT_BOT] = 'DISABLE'
    me = await bot.get_me()
    
    await tgbot.send_message(message.chat_id, "Chat Bot Deactivated")

    kek = await message.get_reply_message()
    id = await bot.get_users(int(message.chat_id))
    session = Lydia.create_session()
    session_id = session.id
    LYDIA_AP.update({str(message.chat_id) + " " + str(id.from_id): session})
    SESSION_ID.update(
            {str(message.chat_id) + " " + str(id.from_id): session_id}
        )


@bot.on_message()
async def user(client, ai):

    ai.text
    if CHAT_BOT == "DISABLE":
        return
    if ai.raw_text.startswith("!ask"): 
     return
    try:
        session = LYDIA_AP[str(ai.chat_id) + " " + str(ai.from_id)]
        session_id = SESSION_ID[str(ai.chat_id) + " " + str(ai.from_id)]
        messages = ai.text
        async with ai.client.action(ai.chat_id, "Typing"):
            text = session.think_thought((session_id, messages))
            wait_time = 0
            for i in range(len(text)):
                wait_time = wait_time + 0.1
            await asyncio.sleep(wait_time)
            await ai.reply(text)
    except KeyError:
        return


@bot.on_message(filters.user & filters.command(["Hi"]))
async def send_welcome(client, message):
      if CHAT_BOT == 'ENABLE':
          return
      ssendr = message.sender_id
      ko=await bot.get_me()
      
      if ssendr == ko.id :
       await tgbot.send_message(message.chat_id, "**Hi! Master If You Want That I Talk!**\n\n**Kindly Enable Chatbot**\n\n**You Can Chat With Me :)**")
      
      else:
       await tgbot.send_message(message.chat_id, "**Hi! How Can I Help?**\n\n**Kindly Leave The Message**\n\n**You Can ask my master by doin !ask :)**")



# @tgbot.on(messages.NewMessage(pattern="^Help"))
# async def send_welcome(event):
#     if CHAT_BOT == 'ENABLE':
#      return
#     user =OWNER # U s k a B a s  c h a l e  t o  s a r a d a r i y a  p i i  j a y e, a a e k h u d a  t u  b o l d e   t e r e   b a d l o  k o 
    
#     sendr = event.sender_id
#     from userbot import bot
    
#     owner=await bot.get_me()
      
#     if sendr == owner.id :
#        await tgbot.send_message(event.chat_id, "**Hi! Master If You Want That I Talk!**\n\n**Kindly Enable Chatbot Then, You Can Chat With Me :)**")
#     else:
#        await tgbot.send_message(event.chat_id, f"**Kindly Leave The Message**\n\n**I Will Pass It To {user}**")


