# Copyright (C) 2021 KeinShin@Github.
import pandas as pd

from system.Config.utils import hd_no
import re
from pyrogram import filters
from system import  *
from better_profanity import profanity
from system.decorators import on_cmd
from system.sqls.pm_sql import *

SPAMMERS = []
LIMIT = []
SPAM_LIMIT = []



@app.on(filters.incoming & filters.private & ~filters.edited & ~filters.me)
async def pm(client, message):
    mister = await app.get_users(int(message.chat_id))
    sed_user = get_id(mister.id)

        
    if mister.id ==sed_user.id:
        return
    if mister.is_bot:
        return
    if mister.is_contact:
        return
    if mister.is_mutual_contact:

        return
    if mister.is_scam:
        alt = language('ALERT')
        scm = language('SCAMMER')
        await bot.send_message(chet, f"__{alt}__!\n**{scm} [{mister.first_name}]({mister.id}) IN PM**")
        await app.send_message(message.chat_id, f"{language('Scammer Alert! Therefore blocked and informed master!')}")
        await app.block_user(message.chat_id)
        return
    if mister.is_fake:
        await app.send_message(message.chat_id, f"**{language('FAKE ID ALERT')}!--")

        return
    if his_turn(mister.id) == PM_LIMIT and not get_user(mister.id) == mister.id:
        await app.send_message(message.chat_id, "__I warned you 5 times now its time for action byy__\n\n**BLOCKED**")
        return
    await app.block_user(mister.id)

    if user_abused(message.text) and not get_user(mister.id) :
    
        await app.send_message(message.chat_id, f"**ABUSE DETECTED! SO BLOCKED FROM PM :)**\n\n__If you think it's mistake use__ {g}")
        await app.block_user(mister.id)
        return

    name=mister.first_name
    bot_results = client.get_inline_bot_results(f"{g}", "**Black")
    await client.send_inline_bot_result(
               message.chat_id,
               bot_results.query_id,
               bot_results.results[0].id
           )


@on_cmd(["a","ap", "approve"])
async def ap(client, message):
    try:
       if hd_no(message.text):
         id = message.text.split()[1]
         await message.edit_message_text(f"{language('APPROVED! USER')} USER - {id}")
         approve_(id)
       elif message.text is None:
         ok= await app.get_users(int(message.chat_id))
         await message.edit_message_text(f"{language('APPROVED! USER')} USER - {ok.first_name}")
         approve_(ok.id)
       else:
         name = message.text.split()[1]
         await message.edit_message_text(f"{language('APPROVED! USER')} - NAME {name}")
   
         approve_(name)
    except BaseException as e:
        await message.edit_message_text(e)



def user_abused(txt):
    return profanity.contains_profanity(txt)



@on_cmd(["da", "disap", "disapprove"])
async def dis(client, message):
    if hd_no(message.text):
      id = message.text.split()[1]
      await message.edit_message_text(f"{language('DISAPPROVED USER - ')} {id}")
      dispprove(id)
    else:
      name = message.text.split()[1]
      await message.edit_message_text(f"{language('DISAPPROVED USER - ')} {name}")
      dispprove(name=name)



@on_cmd(["listapprovd"])
async def list(client, message):
    
    noice=get_approve()
    await app.send_message(message.chat_id, f"{language('**USERS - APPROVED**')}\n\n__{noice}__")






COMMAND_HELP.update({
    "pm_permit": f"`{HNDLR}approve or a `\
    \n`{HNDLR}da or disapprove`\
    \n`{HNDLR}listapprovd`",
    "pm_permit's help": f"`{HNDLR}approve or a `\
    \n**USE**: __Approves user to your pm means he or she can pm you!__\
    \n\n`{HNDLR}da or dispprove\
    \n**USE**: __Disapproves user from your pm!__ `\
    \n\n{HNDLR}listapprovd\
    \n**USE**: __approves user to your pm__"
})
