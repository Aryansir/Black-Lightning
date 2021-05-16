# Copyright (C) 2021 KeinShin@Github.



#  Hello sur 
import time as t


from system.decorators import on_cmd
from system.Config import Variable
from system.Config.utils import  get_readable_time
ping = get_readable_time((t.time() - t.time()))
from system import (ALIVE_IMG, app, ALIVE_MESSAGE, OWNER, time, ttl, updates, self_hosted, mode_type,      
ALIVE_IMG
)        # Easter OwO



@on_cmd(["alive", "black", "alv", f"{OWNER}"])
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

 
