# Copyright (C) 2021 KeinShin@Github.


import os
import string



import io


# with io.BytesIO(str.encode(OUTPUT)) as out_file
            # out_file.name = "cmd_list.text"
import logging
import os

from system import LANG, app
from textblob import TextBlob
from translate import Translator
from dotenv import load_dotenv

try:

 import heroku3
except Exception:
 os.system("pip3 install heroku3")
 


# from var import Var
# herokuclient = heroku3.from_key(Var.HEROKU_API_KEY)
class Variable(object):
    TG_API_ID = os.environ.get("TG_APP_ID", None)
    TG_API_HASH = os.environ.get("TG_API_HASH", None)
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", '12344: dssdsdssd')
    TG_BOT_USER_NAME = os.environ.get("TG_BOT_USER_NAME", None)
    APP_NAME = os.environ.get("APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    ALIVE_ASCII =  os.environ.get("ALIVE_ASCII", None)
    if not ALIVE_ASCII is None:
        pass
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    HNDLR = os.environ.get("HNDLR", ".")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    NO_ROWS_HELP_MENU = os.environ.get("NO_ROWS_HELP_MENU", None)
    if NO_ROWS_HELP_MENU is None:
        NO_ROWS_HELP_MENU = 3
    ENVIRONMENT = os.environ.get("ENVIRONMENT", False)

        
    NO_COLUMNS_HELP_MENU = os.environ.get("NO_COLUMNS_HELP_MENU", None)
    if NO_COLUMNS_HELP_MENU is None:
        NO_COLUMNS_HELP_MENU = 7
    # OWNER_NAME = os.environ.get("OWNER_NAME", None)
    OWNER_NAME = "@keinshin"
    PM_SECURITY_MSG = os.environ.get("PM_SECURITY_MSG", None)
    SUDO_IDS = os.environ.get("SUDO_ID", '12345').split()
    LOGS_CHAT_ID = os.environ.get("LOGS_CHAT_ID", None)
    if PM_SECURITY_MSG is None:
        PM_SECURITY_MSG = (
        f"**Hello User..**"
        f"**{str(OWNER_NAME)} is under Black Lightning PM Security*\n\n"
        f"**Kindly Choose the reason for whcih you came :)** "
    )
    else:
        WARNING = PM_SECURITY_MSG
    HELP_MENU_TXT = os.environ.get("HELP_MENY_TXT", None)
    if HELP_MENU_TXT is not None:
        HELP_MENU_TXT.split()[0]
    else:
        a = "**Black Lightning Help Menu for User**"
        a = HELP_MENU_TXT
    LANGUAGE = os.environ.get("LANGUAGE", None)
    if LANGUAGE is None:
        LANGUAGE = "english"
    

Var = Variable

class Client:
    def __init__(self):
     self.herokuclient = heroku3.from_key(Variable.HEROKU_API_KEY)
# Ported From https://github.com/jaskaranSM/HerokuManagerBot

    
class HerokuHelper:
    def __init__(self, appName, apiKey):
        self.API_KEY = apiKey
        self.APP_NAME = appName
        self.herokuclient = self.getherokuclient()
        self.app = self.herokuclient.apps()[self.APP_NAME]
        
    def getherokuclient(self):
        return heroku3.from_key(self.API_KEY)

    def getAccount(self):
        return self.herokuclient.account()

    def getLog(self):
        return self.app.get_log()

    def addEnvVar(self, key, value):
        self.app.config()[key] = value

    def restart(self):
        return self.app.restart()



class Owner:
    async def __init__(self):
         self.owner = app.me.id

async def errors_s():
    herokuHelper = HerokuHelper(Var.HEROKU_APP_NAME, Var.HEROKU_API_KEY)
    logfuck= herokuHelper.getLog()
    with open("logs.txt", "w") as log:
        log.write(logfuck)
    with open('logs.txt', 'r') as read:
        a =  read.read()
    log.close()
    read.close()
    return a

async def errors2():
    herokuHelper = HerokuHelper(Var.HEROKU_APP_NAME, Var.HEROKU_API_KEY)
    logfuck = herokuHelper.getLog()
    with open("logs.txt", "w") as log:
        log.write(logfuck)
    return 'logs.txt'

    
async def logs():
    herokuHelper = HerokuHelper(Var.HEROKU_APP_NAME, Var.HEROKU_API_KEY)
    logz = herokuHelper.getLog()
    with open("logs.txt", "r") as log:
        wah = log.readline()
    return  wah


def loader():
    pass



# Copyright (C) Midhun KM

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time




def language(text: str):
    # if "**" or "__" or "~~":
    #     a=[i for i in range(len(string)) if string.startswith('**', i)]

    lang = TextBlob(text)
    translator= Translator(from_lang=lang.detect_language(),to_lang=LANG)
    translation = translator.translate(text)
    return translation



def hd_no(txt: str):
    contains_digit = False
    
    
    for character in txt:
    
        if character.isdigit():
    
            contains_digit = True
    
    return contains_digit



class user:
    async def user(self, id):
        self.user_=await app.get_users(int(id))