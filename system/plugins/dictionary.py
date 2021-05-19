from system.Config.utils import Variable
from PyDictionary import PyDictionary
from pyrogram import filters
from system.plugins import light
from system import (
    app,
    COMMAND_HELP,
    HNDLR
)

import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)

mean = ""
@light.on(["dic", "define", "dictonary"])
async def dc(client, message):
    if  not message.text:
        await message.edit_message_text("**How could i define nothing?**")
        return
    txt = message.text.split()[1]
    meana = PyDictionary()
    meaning = meana.meaning(txt)
    for i in meaning['Noun']:
        mean += "\n" + i
    await app.send_message(message.chat_id, f"__Meaning__{mean}")
   
COMMAND_HELP.update({
    "dictionary": f"`{HNDLR}dict or define or meaning`",
    "dictionary's help": "**Gets the meanign of that word from dictonary**"
})


