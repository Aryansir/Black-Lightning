from pyrogram import filters
from pyrogram.types import (   InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup

)

from system.plugins._alive_ea import ping




cap = f"""**υѕєявσт ιѕ αℓινє!
       🇴‌🇼‌🇳‌🇪‌🇷‌-: {OWNER}
       ᴛɪᴍᴇ: {time}
       ᴄᴏᴍᴍᴀɴᴅs: {ttl}
       ᴘɪɴɢ: {ping}
       ᴜᴘᴅᴀᴛᴇꜱ: {updates}
       ꜱᴇʟꜰ ʜᴏꜱᴛᴇᴅ: {self_hosted}
       ᴍᴏᴅᴇ: {mode_type}
       **"""
import os
from system import *

ASSISTANT_PIC = os.environ.get("ASSISTANT_PIC", None)
if ASSISTANT_PIC is None:
       PIC = "https://telegra.ph/file/b5afd12c58bfca1f1d47b.jpg"
else:
       PIC = ASSISTANT_PIC








@bot.on_message(filters.command(["alive"]) & filters.incoming)
async def _(client, event):
    await event.delete()

    await bot.send_document(event.chat_id,
            document=PIC,
            caption=cap,
    )

     




@bot.on_message(filters.command(["alive"]) & filters.incoming & filters.group & filters.via_bot)
async def help(client, message):



       wah = InlineKeyboardMarkup(
       InlineKeyboardButton("Help Menu", callback_data="help")

       )
       await bot.send_document(message.chat_id, document=ALIVE_IMG_ASSISTANT, reply_markup=wah)




@bot.on_callback_query(filters.regex(pattern="help"))
async def hrlp(client, message):
       bot_results = client.get_inline_bot_results(f"{g}", "Assistant Menu")
       await bot.send_inline_bot_result(
               message.chat_id,
               bot_results.query_id,
               bot_results.results[0].id
           )

                       
ASSISTANT_HELP.update({
    "alive": "Users/Admin/Owner Command",
     "alive_bot's Type":  "Owner",
    "alive_bot's Command": f"{HNDLR}alive \
    \n**Usage**: An alive for assistant works in group/Personal Message\
    \nDisclaimer: You should add {g} in the particular group for {HNDLR}alive to trigger in group with Help Menu :p."
})