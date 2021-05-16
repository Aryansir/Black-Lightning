  
# Copyright (C) 2021 KeinShin@Github.


# ME - OK Google,
# Google - * listens *
# Me - Sings a song
# Google - Abe Saale
# XoX 



import pickle
import pandas as pd
from typing import Dict
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import random
from pyrogram.errors.exceptions.bad_request_400 import (MessageIdInvalid,
AboutTooLong,
BotInlineDisabled,





)
import os
from pyrogram.sync import wrap
from system.Config import Variable
from system.Config.utils import *
ERRORS_NAME = []

from pyrogram.types import Message
from system import CMD_LIST, COMMAND_HELP, CMD_DICT, SUDO_USER_NO_OF_TIME_USED
from pyrogram.handlers import MessageHandler


import pyrogram
from system.Config import *
from system.Config.errors import *
from system import app, ASSISTANT_LIST
import logging

time = datetime.datetime.now()

SUDO_USER_NO_OF_TIME_USED = {}
s = []
easters = []
ASSIS_HELP = {}
 # it is test sur
def assistant_command(command: list,
incoming: bool = True,
group: bool = False,
outgoing: bool = False

):
    if incoming is False:
         pyrogram.filters.command(command) & pyrogram.filters.outgoing
    else:
         pyrogram.filters.command(command) & pyrogram.filters.incoming
    try:
       d = " ".join(command) 
       ASSISTANT_LIST.append(d[0:])
    except IndexError:
       pass

    def assistant_dec(func):
        async def wrapper(client, message):
            
            try:
                await func(client, message)
            except BaseException as e:
                logging.error(e)
        return wrapper
    return assistant_dec

def on_cmd(command: list,
         sudo: bool= False,
         sudo_ids = None,
         schedule: bool = False,
         job = None,
         seconds: int = 0
): 
    if Variable.HNDLR is None:
        raise HNDLRERROR(f"{language('You are  not allowed to leave HNDLR None.')}")
    if sudo is True:

        sudo_id = Variable.SUDO_IDS
        filters_ = (
            (pyrogram.filters.me | pyrogram.filters.user(sudo_id)) & pyrogram.filters.command(command, Variable.HNDLR) & ~pyrogram.filters.via_bot
            & ~pyrogram.filters.forwarded
        )
    else:
        filter_ = (
            (pyrogram.filters.me | pyrogram.filters.user("self")) & pyrogram.filters.command(command, Variable.HNDLR) & ~pyrogram.filters.via_bot
            & ~pyrogram.filters.forwarded
        )
    try: 
      c = " ".join(command)
      CMD_LIST.append(c[0:])
    except BaseException as e:
        logging.info(e)
    
    
        def decorators(func):
            async def wrapper(client, message):
                try:
                    await func(client, message)
                    logging.info(
                            f"**{language('Processing Command.')}**"
                        ) 
                except MessageIdInvalid:
                    logging.info(f"{language('User deleted the message while processing')} {func.__module__}")
                    pass
                except AboutTooLong as a:
                    logging.info(f"Demn Too long about :/, {a}")
                    pass
                except BotInlineDisabled:
                    logging.info(f"{language(f'Error as inline is diabled so you can not access command {func.__module__}. Turn inline on for your bot')}: {Variable.TG_BOT_USER_NAME}")
                
                    pass
                except BaseException:
                    ok = str(func.__module__)
                    ERRORS_NAME.append(ok)
                kool = Owner()
                if sudo == True:
                    if not kool.is_self:

                        for i  in sudo_id:
                            s.append(i)
                        SUDO_USER_NO_OF_TIME_USED.update({f"{func.__module__}": s,
                                                            "Time": time},
                                                         )
                        a = pd.DataFrame(SUDO_USER_NO_OF_TIME_USED)

                if ok.endswith("_ea"):
                    eas = ok.split()
                    for i in eas:
                        easters.append(i)
                    pickle.dump(easters, open("easter.dat", "wb"))

          
                app.add_handler(MessageHandler(wrapper, filters=filter_))
        
                return wrapper
        return decorators

# pyrogram.types.User.last_online_date()




def schedule(job,
stime:int = 0,
time = None,
name = None
):
        if time == "seconds":
  
            scheduler = AsyncIOScheduler()


            
            scheduler.add_job(job, 'interval', seconds=int(stime), id=name)
        if time == "minute":    
            scheduler.add_job(job, 'interval', minute=int(stime), id=name)
from system import bot

# function


def owner(func):
    async def wrapper(client, message):
       user = await app.get_users(int(message.chat.id))
       if user.is_self:
           message.answer(f"{language('Only for the strangers not for the owner')}!")
       try:
            await func(client, message)
       except BaseException as e:
            logging.error(e)
    return wrapper

def inline_help_wrapprs(func):
    async def wrapper(client, really):
        bot = await bot.get_me()
        i = await bot.id
        if really.from_user.id == i:
           really.answer(f"{language('Get Lost Retard')}", cache_time=0, show_alert=True)
        else:
            
            try:
                await func(client ,really)
            except Exception as e:
                logging.error(e)  

    return wrapper 




async def scheduler(message,
shutdown:bool =False,
resume:bool = False):
    scheduler = AsyncIOScheduler()
    scheduler.pause()
    await message.edit_message_text(f"**All! {language('scheduling task that are paused')}**.")
    if shutdown is True:
     try:   
        scheduler.shutdown()
        await message.edit_message_text(f"**{language('scheduler is shutdowned')}**")
     except Exception as e:
         await message.edit_message_text(e)
    elif resume is True:
        try:
            scheduler.resume()
            await  message.edit_message_text(f"**{language('All tasks are resumed')}**")
        except Exception as e:
           await message.edit_message_text(e)

