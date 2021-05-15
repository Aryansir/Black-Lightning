# Copyright (C) 2021 KeinShin@Github.



#  Hello sur 
import time

from system.decorators import on_cmd
from system.Config import Variable
from system.Config.utils import  get_readable_time
ping = get_readable_time((time.time() - time.time()))
from system import *              # Easter OwO
@on_cmd(["alive", "black", "alv", f"{OWNER}"], sudo=True, sudo_id=Variable.SUDO_IDS)
async def alive(client, message):
 if ALIVE_MESSAGE is not None:

   text = f"""ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ is ᴀᴡᴀᴋᴇɴᴇᴅ
   🇴‌🇼‌🇳‌🇪‌🇷‌-: {OWNER}
   ᴛɪᴍᴇ: {time}
   ᴄᴏᴍᴍᴀɴᴅs: {ttl}
   ᴘɪɴɢ: {ping}
   ᴜᴘᴅᴀᴛᴇꜱ: {updates}
   ꜱᴇʟꜰ ʜᴏꜱᴛᴇᴅ: {self_hosted}
   ᴍᴏᴅᴇ: {mode_type}
   """
 else:
   text = ALIVE_MESSAGE
 await app.send_document(message.chat_id, ALIVE_IMG, caption=text)
 

