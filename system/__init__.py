# Copyright (C) 2021 KeinShin@Github.



import pandas as pd
import pickle # Yum OWO
from pyrogram import Client
from pyrogram.errors import BotInvalid, AccessTokenExpired, AccessTokenInvalid
from Config import *
import logging
import os
import requests
import datetime
from Config.utils import language
from Config.errors import *
# try:


modes = {
    "modes": ["Friendly", "Aggressive"]
}
pd.DataFrame(modes)

url = "https://elements.heroku.com/buttons/keinshin/black-lightning"


app = Client(Variable.STRING_SESSION, Variable.TG_API_ID, Variable.TG_API_ID,)
# except 
if Variable.TG_BOT_TOKEN:
  try: 
     bot = Client(
             "HELPER",
             api_id=Variable.TG_API_ID,
             api_hash=Variable.TG_API_ID,
             bot_token=Variable.TG_BOT_TOKEN,
             sleep_threshold=180)
  except BotInvalid as e:
     logging.info(e)
     pass

  except AccessTokenExpired:
    logging.info("Invalid bot token.")
    pass
else:
    raise BotTokenError('Error. Bot Token not found!')
g =  Variable.TG_BOT_USER_NAME

OWNER = language(Variable.OWNER_NAME)
chet = Variable.LOGS_CHAT_ID
time = datetime.datetime.now()
CMD_LIST = []
ttl = len(CMD_LIST)
REPO = os.environ.get("GIT_REPO_NAME", None)
if REPO is None:
      REPO = "https://github.com/KeinShin/Black-Lightning"
BRANCH = os.environ.get("BRANCH", None)

APP_NAME = Variable.HEROKU_APP_NAME
API_KEY = Variable.HEROKU_API_KEY
HNDLR = Variable.HNDLR
CMD_DICT = {}
COMMAND_HELP = {}
ASSISTANT_HELP = {}
ASSISTANT_LIST = []
SUDO_USER_NO_OF_TIME_USED = {}
last_up = time.time()


# LANG = Variable.LANGUAGE
LANG = "english"
ALIVE_MESSAGE = os.environ.get("ALIVE_MESSAGE", None)
ALIVE_IMG = os.environ.get("ALIVE_IMG", None)
PM_LIMIT = os.environ.get("PM_LIMIT", None)
if PM_LIMIT is None:
    PM_LIMIT = "5"




if ALIVE_IMG is None:
    ALIVE_IMG = "https://telegra.ph/file/4e83650cf1e3e8c31c51b.mp4"

MODE = os.environ.get("MODE", None)
if MODE is None:
   a=language('Friendly')
   MODE = f"**{a}**" # :P
else:
   mode_type = MODE
self_hosted = Path('exconfig.py').is_file()
if self_hosted:

      self_hosted = language("True")
else:
      self_hosted = language('False')


accha = open("updates.txt")
if "Nope" in accha:

 updates =  language('NO-UPDATES') + 'XoX' # XoX
else:
 updates=language('UPDATES AVAILABLE!')





ALIVE_IMG_ASSISTANT = os.environ.get("ALIVE_IMG_ASSISTANT", None)
if ALIVE_IMG_ASSISTANT is None:
    ALIVE_IMG_ASSISTANT = "https://telegra.ph/file/4e83650cf1e3e8c31c51b.mp4"
