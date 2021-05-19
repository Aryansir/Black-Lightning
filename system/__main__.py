# Copyright (C) 2021 KeinShin@Github.
import subprocess

import os.path
import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from setup.importer import Start
import pickle as yum
import logging 

import schedule
from pyrogram.handlers import MessageHandler

from pyrogram import idle
from system.Config.utils import Variable
from pyrogram.raw.types import BotCommand
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
import holidays
from datetime import date, datetime
if Variable.COUNTRY:
    
   hol  = holidays.CountryHoliday(Variable.COUNTRY)
else:
   hol = holidays.CountryHoliday("IN", prov="AS")
a = date.today()
p  =hol.get(a)



plugin =  logging.getLogger("PLUG-ERROR")
bot_lod =  logging.getLogger("BOT-ERROR")


from system.__init__ import app, bot



chet = Variable.LOGS_CHAT_ID


USER = str(Variable.OWNER_NAME)

async def easter():
    # if Variable./
    est=yum.load("easters.dat", "rb") # for easters!
    if len(est)==7:
        await bot.send_message(chet, "**Congo**, **You have unlocked all the easters of this userbot gib party sir** 🎉🎆")

async def holydays():
    if p:
        await bot.send_message(chet, f"Happy {p} Master ✨🎉☺")
    else:
        return None


schedule.every().day.at("12:00").do(holydays)



async def add_bot_to_logg_grup(client, message):
    try: 

        await bot.join_chat(chet)
        text = f"BLACK USERBOT is deployed."
        async with message.reply_chat_action("typing"):

           await bot.send_message(chet, text)
    except BaseException:

        logging.error("CANNOT ADD ASSISTANT TO LOGS CHAT")
        pass
        


import glob
import importlib

def finnalise():
        




        info = f"Everything is loaded, starting userbot and adding  bot  to LOG CHANNEL "
        try:
         app.start()
         bot.start()
        except Exception as e:
         logging.error(f"CANNOT LOAD USER DUE TO {e}")
         exit()
        a  = Start("system/plugins/")
        a.boot()
        b = Start("system/user_bot_assistant/")
        b.boot()
        logging.info(info)
        app.send_message("me", f"**BLACK-LIGHTNING USERBOT's MESSAGE\n\n{USER} Kindly Enable Inline from @BotFather to Access All The Features Including `.help` and Many More (if it's already done Ignore this message)")
        
        idle()

if __name__ == "__main__":
    finnalise()


