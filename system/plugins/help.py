# Copyright (C) 2021 KeinShin@Github.








# import sys
# import os
# from sys import path
# dir_path = "/absolute/path/to/E:\on_cmd-UserBot"
# sys.path.insert(0, dir_path)
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pyrogram.methods import messages


from system.Config import Variable
from system.decorators import ERRORS_NAME, on_cmd
from system import CMD_LIST, COMMAND_HELP, bot, app, SUDO_USER_NO_OF_TIME_USED
from pyrogram.errors import BotInlineDisabled
import logging
import pandas as pd

HNDLR = str(Variable.HNDLR)

g =  Variable.TG_BOT_USER_NAME
string = ""
# unofficial_or_no_help = 0
@on_cmd(["help"])
@on_cmd(["help"], sudo=True, sudo_id=Variable.SUDO_IDS)
async def helper(client, message):
        count = 0

 
        if " " in await message.text:
          text = await  message.text.split()[1]
          try:
             for i in CMD_LIST:
                 string += HNDLR +  i + "\n"
                 string += "\n"
                 count += 1
             await message.edit_message_text(f"🐱‍🚀** {count} Commands in {text}**🐱‍🚀\n\n`{i}`")
          except KeyError:
            await message.edit_message_text(f"**ERROR! No MODULE with name {text} either it is not available**")
            return
          except BaseException as e:
            await message.edit_message_text(f"ERROR!: {e}")
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
             await message.edit_message_text(f"**Bot {g}  inline is disabled turn it on!**")
             return
           except BaseException as a:
             logging.error(a)
             await  message.edit_message_text(f"**ERROR** - `{a}`\n\n**Occured while  opening help menu try doing** __@{g} Help Menu__\n\n**if help not appears contact @lightning_support_grup**")
    

@on_cmd(["errorcmds"], sudo=True, sudo_id=Variable.SUDO_IDS)
async def error(client, message):    
  error_cmd = ""
  cou = 0
  for  i in ERRORS_NAME:
      error_cmd += i
      error_cmd += "\n"
      cou += 1
  await message.edit_message_text(f"**Total commands which was having error few times ago or currently are {cou}**\n\n`{error_cmd}`")



a = pd.DataFrame(SUDO_USER_NO_OF_TIME_USED)


@on_cmd(['sudo'])
async def used(client, message):


  horny_man = await message.text
  if  await message.text is None:
    await message.edit_message_text("**Gib some input :/**")
    return
  if " " in await  message.text:
    messagec = await  message.text.replace("sudo", "")
    text = messagec.split(",")
    name=text[1] 
    # text =  message.text.split()[1
    used = ""
    # a = pd.DataFrame(SUDO_USER_NO_OF_TIME_USED)
    s=a.loc[:, ['{}'.format(name), 'Time']]
    k=s.to_string(index=False)
    b = a[text]
    await app.send_message(message.chat_id, "**Number ids who have used or using** __{}__ **are**\n\n`{}`".format(name, k))
  elif "," in horny_man:
    messagec = await message.text.replace(f"{HNDLR}sudo", "")
    text = await messagec.split(",")
    name=text[0] 
    id = text[1]
    module_name=text[2]
    user =  await app.get_users(int(id))
    sed_user = a.loc["{}".format(module_name) == id]
    await app.send_message(message.chat_id, f"SUDO USER {user.first_name}]({id})\n{sed_user}")
  else:
    await message.edit_message_text(f"Gib some module name and user id  to check :/\n\n**Syntax: __{HNDLR}sudo_cmds id,name ( dont forget that ',' )")




COMMAND_HELP.update({
  "help": f"`{HNDLR}help` (command) or {HNDLR}help\
  \n\n`{HNDLR}sudo` (username)",
  "help's help": f"**USE**: {HNDLR}help (command) gets the detailed help without triggering help menu and {HNDLR}help triggers help menu\
  \n\n`{HNDLR}sudo (username)` **will get the names who've used sudo plugins whom which you have given access."
})
