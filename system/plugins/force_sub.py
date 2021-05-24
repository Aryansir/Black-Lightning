
 # Copyright (C) 2021 KeinShin@Github.



from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from system.plugins import light
from system import COMMAND_HELP, HNDLR, app, bot
from pyrogram import filters
from system.sqls.chat_sql import *

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions, CallbackQuery

@light.on(["forcesub"])
async def force(client, message):
    
    try:
     txt = message.text.split()[1]
     name = message.text.split()[2]
    except IndexError:
        await message.edit(f"**Correct Syntax**: `{HNDLR}forcesub (channel user name) ( group user name )`")
    if  chats(exsis=True) == "no chats":
        await message.edit("**You can only enable force subscribe in one channel and one group at a time**")
        return
    try:
        await message.edit(f"**Force Subscribe enable** for channel {name} in group {txt} ")
        add_chat(txt, name)
    except BaseException as e:
        await message.edit(f"**ERROR** - {e}")


@bot.on_message(filters.chat(chats()))
async def sub(client, message):

    user = await app.get_users(message.chat.id)
    if  exists(user.id):
        return
    try:
     check = app.get_chat_member(chats(), user.username)
     add_user(check['id'])
    except UserNotParticipant:
        await bot.restrict_chat_member(message.chat.id, user.id, ChatPermissions(can_send_messages=False))

        mkp = InlineKeyboardMarkup(
                [[InlineKeyboardButton("Unmute", callback_data="chata")]]
            ),
        await bot.send_message(message.chat.id, f"You havent subscribe {chats()}. Go and Subscribe Now! then press un-mute", reply_markup=mkp)
     

@bot.on_callback_query(filters.regex(pattern="chata"))

async def detailed(client, chet: CallbackQuery):

    user = await app.get_users(chet.id)
    try:
     check = app.get_chat_member(chats(), user.username)
     add_user(check['id'])
     await chet.delete()
     await bot.restrict_chat_member(chats(), user.username, ChatPermissions(can_send_messages=True))

    except UserNotParticipant:
      await chet.answer("You havent subscribed yet!", show_alert=False)



COMMAND_HELP.update({
    "force_sub": f"`{HNDLR}forcesub` **(group) (channel)**"
})
