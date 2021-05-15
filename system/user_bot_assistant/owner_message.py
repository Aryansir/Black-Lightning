from system.Config.utils import Owner
from system import app, bot
from pyrogram import filters

from system.Config import Variable
p = await Owner()
owner= filters.create(func=p.owner, name="Owmer")




@bot.on_message(
    filters.private
    & filters.incoming
    & owner
    & ~filters.edited
)
async def owner(client, message):
    pass
