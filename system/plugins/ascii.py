# Copyright (C) 2021 KeinShin@Github.

from art import *
from system.decorators import on_cmd
from system import app, HNDLR, COMMAND_HELP
from system.Config.utils import language
from system.Config import Variable





@on_cmd(["ascii"])
@on_cmd(["ascii"], sudo=True, sudo_id=Variable.SUDO_IDS)
async def ascii(client, message):
    txt=message.text.split()[1]
    msg= message.text
    if msg is None:
        a=art("random")
        await message.edit_message_text(a)
    if " " in msg:
        ar = art(txt)
        await message.edit_message_text(ar)

    
COMMAND_HELP.update({'ascii': f"""{HNDLR}ascii or {HNDLR}ascii (text)""",
                     "ascii's help": f"""**USE**:- __{language("Creates random ascii art faces if it's 'NONE' else same face as your given condition")}__ OWO"""})
