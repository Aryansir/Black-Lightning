from system import bot
# from zeda.user_bot_assistant._admin_prev import Admin, session
ASSISTANT_HELP = {}
import os, asyncio 
ASSISTANT_CMD_HNDLR = os.environ.get("ASSISTANT_CMD_HNDLR", None)
if ASSISTANT_CMD_HNDLR is None:
    ASSISTANT_CMD_HNDLR = "/"
else:
   ass_cmd_hndlr = ASSISTANT_CMD_HNDLR


# rnk_name, r = Admin()

async def cmd():
    commn = "ls zeda/plugins/thunder"
    process = await asyncio.create_subprocess_shell(
        commn, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    o=o.split()

    return len(o)


# class oowner:
      
#   async def very_Ded(self):
#        self.wah=await bot.get_me()
#        return self.wah
  

# class Rank:
#     def __int__(self, num):
#         if num == 5 or 5<num:
#             a = Admin()
#             ranko =  Admin(fullname='Ed Jones', nickname='edsnickname')
#             return 