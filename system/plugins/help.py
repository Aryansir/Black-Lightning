# Copyright (C) 2021 KeinShin@Github.








# import sys
# import os
# from sys import path
from nltk.util import Index
from pyrogram.methods import messages


from system.Config import Variable
from system.decorators import ERRORS_NAME, light
from system import CMD_LIST, COMMAND_HELP, bot, app, SUDO_USER_NO_OF_TIME_USED
from pyrogram.errors import BotInlineDisabled
import logging
import pandas as pd

HNDLR = str(Variable.HNDLR)

g =  Variable.TG_BOT_USER_NAME
string = ""
# unofficial_or_no_help = 0
@light().on(["help"])
async def helper(client, message):
        count = 0
        try:

         txt = message.text
        except IndexError as e:
          await message.edit(e)
        if " " in  txt:
          text = message.text.split()[1]
          try:
             for i in CMD_LIST:
                 string += HNDLR +  i + "\n"
                 string += "\n"
                 count += 1
             await message.edit(f"🐱‍🚀** {count} Commands in {text}**🐱‍🚀\n\n`{i}`")
          except KeyError:
            await message.edit(f"**ERROR! No MODULE with name {text} either it is not available**")
            return
          except BaseException as e:
            await message.edit(f"ERROR!: {e}")
        else:
           try:
                if not g.startswith("@"):
                  logging.error("You should have '@' with your bot's username eg -:@{} not like -: {}".format(g, g))
                  return
                await message.delete()    
                bot_results = client.get_inline_bot_results(f"{g}", "Help Menu")
                await client.send_inline_bot_result(
               message.chat_id,
               bot_results.query_id,
               bot_results.results[0].id
           )
           except BotInlineDisabled:
             await message.edit(f"**Bot {g}  inline is disabled turn it on!**")
             return
           except BaseException as a:
             logging.error(a)
             await  message.edit(f"**ERROR** - `{a}`\n\n**Occured while  opening help menu try doing** __@{g} Help Menu__\n\n**if help not appears contact @lightning_support_grup**")
    
