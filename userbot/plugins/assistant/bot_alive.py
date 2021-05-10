from telethon import events, Button

from userbot import ALIVE_NAME, bot, custom 

currentversion = "4.9"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Black Lightning"
PM_IMG = "https://telegra.ph/file/7f72b0ea1893e84028298.mp4"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += f"➥ **Version** : `{currentversion}`\n"
pm_caption += f"➥ **My Master** : {DEFAULTUSER} \n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](https://github.com/KeinShin/Black-Lightning/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : [Raiden-devs](GitHub.com/Raiden-Devs)\n"
light = [[Button.url("Repos", "https://github.com/KeinShin/Black-Lightning"), Button.url("Support", "https://t.me/lightning_support_group")]]
light +=[[custom.Button.inline("Help", data=re.compile(b"gibcmd"))]]
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption, buttons=light)
