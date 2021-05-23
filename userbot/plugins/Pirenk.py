BOT = "Black Lightning Userbot"
from telethon import events, Button, custom
import os,re, asyncio
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(cs))
async def inline_id_handler(event: events.InlineQuery.Event):
 builder = event.builder
 X=  [custom.Button.inline("🔥 CLICK ME 🔥",data="randwa")]
 query = event.text
 result = builder.article(title='Lightning Mejik',text="MASTER TAP ME AND SEE MEJIK",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"randwa")))
async def hmm(event):
    if event.query.user_id == bot.uid:
        text = "Black Lightning Here Master \n Searching Chutia Peoples in this chat for you😘"
        await event.answer(text, alert=True)
        await bot.send_message(event.chat_id, "YEAH MY MASTER TAPPED ME")
    else:
        txt = f"Ja na Lawde \nBhosadike bete \nMadarchod \nInsaniyat ke dhabbe \n{BOT} Tere liye ni he\nVapas apni Suar jesi shakal uthae mat aana"
        await event.answer(txt, alert=True)
        OK = event.query.user_id
        X= await bot.send_message(event.chat_id, f"YE MERE OP MASTER NI HE YE KOI AUR\nHE PATA LAG GYAA MASTER YE TO  [CHUTIA](tg://user?id={ok}) HE \nWAIT KARO MASTER ABHI DM ME ISKI GAND CHEEL KE AATA")
        await asyncio.sleep(10)
        for i in range (1):
           await bot.send_message(OK, "TUNE BUTTON KO TAP KAISE KIYA BE TERE BAAP KA HE WO BUTTON ?")
