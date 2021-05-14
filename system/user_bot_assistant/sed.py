from telethon import TelegramClient
from telethon import *
oh = ["@keinshin", "me"]
s=", ".join(oh)
# async def ohs():
#     acc = 0

#     for i in range(0, len(oh)):
#       acc += 1
#       k=oh[acc]
  
#       await a.send_message(k, "Hi")

# a.loop.run_until_complete(ohs())
tgbot = TelegramClient('bot', 2542398, "fd14f082a108af90513d7689a60ba71f").start(bot_token="1681068353:AAHBWaximTfW3ju5_VVVzEJBdGgvSe1qV2s")

@tgbot.on(events.NewMessage(pattern=f"^Hello", from_users=s))
async def o(event):
    await tgbot.connect()

    await tgbot.send_message(event.chat_id, "HI")
    tgbot.run.loop.run_until_complete()