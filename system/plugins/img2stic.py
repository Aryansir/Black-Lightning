from system.decorators import on_cmd

from system import *


@on_cmd(["img2stic"])
async def img2(client, message):
    bot = "@buildstickerbot"
    await app.send_message(bot, "/start")
    await app.send_message(bot)



COMMAND_HELP.update(
    {"img2stic": f"{HNDLR}img2stic",
    "img2stic's help": "Creates image to sticker!"
    }
    
)