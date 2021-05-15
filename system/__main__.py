# Copyright (C) 2021 KeinShin@Github.
import subprocess

import os.path
import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pickle as yum
import logging 

import schedule

import pyrogram


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

from system.Config import Variable


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



async def add_bot_to_logg_grup():
    try: 

        await bot.join_chat(chet)
        text = f"BLACK USERBOT is deployed."
        async with bot.send_chat_action(chet, action="Typing"):
           await bot.send_message(chet, text)
    except BaseException:

        logging.error("CANNOT ADD ASSISTANT TO LOGS CHAT")
        


import glob
import importlib

async def start():

        await app.start()
#         os.system("chmod +x sh_files/load.sh")
#         os.system("chmod +x sh_files/assist.sh")
        os.system("bash sh_files/load.sh")
        os.system("bash sh_files/assist.sh")
        info = f"Everything is loaded, Black Lightning is Online check your saved message and bot is added to LOG CHANNEL "
        
        logging.info(info)
        
        await pyrogram.idle()
        await  app.send_message("me", f"**BLACK-LIGHTNING USERBOT's MESSAGE\n\n{USER} Kindly Enable Inline from @BotFather to Access All The Features Including `.help` and Many More (if it's already done Ignore this message)")


app.loop.run_until_complete(add_bot_to_logg_grup())

app.loop.run_until_complete(start()) 
