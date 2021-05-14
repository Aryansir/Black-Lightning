from Config.utils import Owner
from system import *
from pyrogram import *

from Config import *
p = Owner()
owner= filters.create(func=p.owner, name="Owmer")




@bot.on_message(
    filters.private
    & filters.incoming
    & owner
    & ~filters.edited
)
async def owner(client, message):
    pass