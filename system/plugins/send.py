# Copyright (C) 2021 KeinShin@Github.

from system.Config.utils import Variable
from system import light


from system import *
@light.on(["send"])
async def send(client, message):
    try:
        txt=message.text
    except IndexError:
        await message.edit(f"**Syntax**: __{HNDLR}send (file name)__\n\n@lightning_support_grup")
    if not " " in message.text:
        await message.edit(f"**Syntax**: __{HNDLR}send (file name)__\n\n@lightning_support_grup")
        return
    txt=message.text.split()[1]

    if  Path(f'{txt}.py').is_file():
        path = f"./system/plugins/{txt}.py"
        await app.send_document(message.chat.id, document=path, caption=f"**PLUGINS** - __{txt}__\n\n@lightning_support_grup", force_document=True)
    elif "sql" in message.text:
        if not Path(f'{txt}.py').is_file():
            await message.edit("**SQL DOES NOT EXSISTS!**")
        else:
           path = f"./system/sqls/{txt}.py"
           await app.send_document(message.chat.id, document=path, caption=f"**SQL-FILE** - __{txt}__\n\n@lightning_support_grup", force_document=True)
    elif "requirements" in message.text:
        path = f"{txt}.txt"
        await app.send_document(message.chat.id, document=path, caption=f"**REQUIREMENTS-FILE** - __{txt}__\n\n@lightning_support_grup", force_document=True)
    else:
        await message.edit("{} does not exsists! (make sure name is correct :/)".format(txt))
    await message.delete()


COMMAND_HELP.update({
    "send": f"`{HNDLR}send` (file name)",
    "send's help": f"\n\n**USE**: __sends the given command/requirements/sql file__"
})
