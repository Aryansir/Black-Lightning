# Copyright (C) 2021 KeinShin@Github.

from system.Config.utils import Variable
from system.decorators import on_cmd


from system import *
@on_cmd(["send"], sudo=True, sudo_ids=Variable.SUDO_IDS)
async def send(client, message):
    if not " " in message.text:
        await message.edit_message_text(f"**Syntax**: __{HNDLR}send (file name)__\n\n@lightning_support_grup")
        return
    txt=message.text.split()[1]

    if  Path(f'{txt}.py').is_file():
        path = f"./system/plugins/{txt}.py"
        await app.send_document(message.chat_id, document=path, caption=f"**PLUGINS** - __{txt}__\n\n@lightning_support_grup", force_document=True)
    elif "sql" in message.text:
        if not Path(f'{txt}.py').is_file():
            await message.edit_message_text("**SQL DOES NOT EXSISTS!**")
        else:
           path = f"./system/sqls/{txt}.py"
           await app.send_document(message.chat_id, document=path, caption=f"**SQL-FILE** - __{txt}__\n\n@lightning_support_grup", force_document=True)
    elif "requirements" in message.text:
        path = f"{txt}.txt"
        await app.send_document(message.chat_id, document=path, caption=f"**REQUIREMENTS-FILE** - __{txt}__\n\n@lightning_support_grup", force_document=True)
    else:
        await message.edit_message_text("{} does not exsists! (make sure name is correct :/)".format(txt))
    await message.delete()


COMMAND_HELP.update({
    "send": f"`{HNDLR}send` (file name)",
    "send's help": f"\n\n**USE**: __sends the given command/requirements/sql file__"
})
