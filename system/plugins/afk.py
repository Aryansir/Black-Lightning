# Copyright (C) 2021 KeinShin@Github.



from system.plugins import light
from system.Config import Variable
from system import (
  app,
  g,
  bot,
  a
)
from system.Config.utils import language

from pyrogram import filters
create = open("afk.txt", "a")
reading_file = open("afk.txt", "r")
if "False" in reading_file:
      txt = "False"
      txs = "True"
else:
    txt = "True"
    txs  = "False"



@light.on(["afk"], sudo_ids = Variable.SUDO_IDS)
async def _(client, message):
  new_file_content = ""
  for line in reading_file:
    stripped_line = line.strip()
    new_line = stripped_line.replace(txt, txs)
    new_file_content += new_line +"\n"
  reading_file.close()
  writing_file = open("updates.txt", "w")
  writing_file.write(new_file_content)
  writing_file.close()


@app.on_message(filters.me  & filters.mentioned & filters.all & filters.outgoing)
async def n(client, message):
  if "False" in reading_file:
    return
  user = await app.get_users(int(app.get_me().id))
  if " " in a:
        
   res = message.text.split()[1]
  else:
   res = ""
  if res:
      text = language("**Master is afk from** {}\n\n~Reason~ - __{}__".format(user.last_online_date, res)) 

  else:
      text = language(f"__I'm afk till i'm done with my tasks contact me via {g}")
  await bot.send_message(message.chat_id, text)





# WeW thanks for visit TWT
