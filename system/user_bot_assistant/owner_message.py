from Config.utils import Owner
from system import app, bot
from pyrogram import filters

from Config import Variable
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