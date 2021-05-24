#work in progress 
#kangers stay away n fuk your mothers
#Copyright (C) 2021 Raiden-Devs@Github


from var import Var
from userbot.utils import lightning_cmd, bot
from resources import photo_2020-12-19_18-34-41.jpg as lem

from userbot import ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"
@bot.on(lightning_cmd(pattern="Devbot"))
    await event.edit("Assistant Bot Devloping Master Keep Patience😉")
async def _(event):
  name=Var.TG_BOT_USER_NAME_BF_HER
  async with bot.conversation("@BotFather") as conv:
    await conv.send_message("/setinline")
    await conv.get_response()
    await conv.send_message(name)
    await conv.get_response()
    await conv.send_message("Heya Master Type here Something")
    await conv.send_message("/setname")
    await conv.get_response()
    await conv.send_message(name)
    await conv.get_response()
    await conv.send_message("{DEFAULTUSER}'S αѕѕιѕтαηт")
    await conv.get_response()
    await conv.send_messssage("/setdescription")
   
    await conv.get_response()
    await conv.send_message(name)
     await conv.get_reponse()
    await conv.send_message("Heyy there,🤙\nThis Black Lightning Userbot🇮🇳\nI am here to provide Assistant service to {DEFAULTUSER}😎\nYou can Message me to contact my Master😉")
     await conv.get_reponse()
    await conv.send_message("/setabouttext")
     await conv.get_reponse()
    await conv.send_message(name)
    await conv.get_reponse()
    await conv.send_message("I am {DEFAULTUSER}'s Assistant You can Use me to conact him")
   #bot pic import kese karte????
    #await conv.get_reponse()
   # await conv.send_message("/setbotpic)
   # await conv.get_reponse()
   # await conv.send_message(name)
   # await conv.get_reponse()
   # await conv.send_message(lem)
    
    respond = await conv.get_response()
  await event.edit("Bot Already Master you can check it {name}") 
