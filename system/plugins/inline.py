# Copyright (C) 2021 KeinShin@Github.

import os
from pyrogram.methods.utilities import remove_handler

from pyrogram.types.messages_and_media import message
from system.Config import Variable as Var
from pyrogram.types import (   InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineQuery



)

ASISTANT_CMD_ROWS = os.environ.get("ASISTANT_CMD_ROWS", None)
if ASISTANT_CMD_ROWS is None:
   number_of_rows_in_commands = 6







ASISTANT_CMD_COLUMNS = os.environ.get("ASISTANT_CMD_COLUMNS", None)
if ASISTANT_CMD_COLUMNS is None:

   number_of_columns_in_commands = 3

from system import *
from math import ceil
from pyrogram import filters

Friends = {}
from system.Config.utils import language, errors2, errors_s
from system.decorators import inline_help_wrapprs, owner

plugs = []
tgbot = bot
g = Variable.TG_BOT_USER_NAME
USER = str(Var.OWNER_NAME)

PM_MSG = os.environ.get("PM_MSG", None)
if PM_MSG is None:
    BOT_LIT = f"Hello Sir MySelf Black Lightning Here For  {USER}'s Protection "
else:
    BOT_LIT = PM_MSG   


PM_PIC = os.environ.get("PM_PIC", None)
if PM_PIC is None:
    PM_SECURITY_IMG = "https://telegra.ph/file/07d55d71944a852ac6d5e.jpg"
else:
    PM_SECURITY_IMG = PM_PIC





LIST = []

a = [x for x in os.listdir("system/plugins/") if x.endswith(".py") and not x.startswith("__")]
for i in a:

  LIST.append(i)

sa = [x for x in os.listdir("system/user_bot_assistant/") if x.endswith(".py") and not x.startswith("__")]
for i in sa:

  ASSISTANT_LIST.append(i)

@bot.on_inline_query()




async def inline_handler(client, inline_query: InlineQuery):
    fuking_sucking = await app.get_me()
    a = fuking_sucking.id
    text = inline_query.query
    if text == "Menu":
        content = InputTextMessageContent("**Black Lightning Help Menu for User** [{}]({})".format(USER[1:],  f"tg://user?id={fuking_sucking.id}"))



        await client.answer_inline_query(
                inline_query.id,
                cache_time=1,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="Help",
                            input_message_content=InputTextMessageContent(
                                f"**Black Lightning Help Menu: COMMANDS: {len(LIST)}**"
                            ),
                            reply_markup=InlineKeyboardMarkup(help_menu(0, LIST, "help")),
                        )
                    )
                ],
            )
    elif inline_query.from_user.id == a and text.lower() == "need" and "Traceback" in errors_s():
       
        await client.answer_inline_query(inline_query.id,
            cache_time=0,
            results = InlineQueryResultArticle(
        
 
              "Click for the help",
              text=f"**How If you Faced Problem \n{USER}** \nChoose Your Problem For Help ",
              reply_markup=
                InlineKeyboardMarkup(
                [InlineKeyboardButton("Commands Not Working🥺", url="https://t.me/lightning_support_grup")],
                [InlineKeyboardButton("Help Article 🤓", url="https://app.gitbook.com/@poxsisofficial/s/help/")],
                [
                    InlineKeyboardButton(
                
                    "Want To Learn CMDS😅",
                    url="https://t.me/lightning_support_grup" ,
                    )
                ], )
              )
             )
              
              

    elif text == "**Black":
        mrkup=[(

                [   InlineKeyboardButton(
                        f"{language('My Friend')}❤️❤️",
                        callback_data ="he_sucks",
                    )
                ],
                [InlineKeyboardButton(f"{language('Request')}🙏", callback_data ="fck_ask")],
                [
                    InlineKeyboardButton(
                        f"{language('Urgent')}", 
                        callback_data ="urgent",)
                        
          ],)
          ]
  
        await client.answer_inline_query(
            inline_query.id,
            cache_time=1,
            results=InlineKeyboardMarkup(mrkup)

        
        )
    # elif  text == "Assistant Menu":
    #     fucking_sucking = await bot.get_me()
    #     text = inline_query.query
    #     content = InputTextMessageContent("**Black Lightning ASSISTANT Help Menu for User** [{}]({})".format(USER[1:],  fucking_sucking.id))
        # await inline_query.answer(result=[
        # InlineQueryResultArticle(
                    
        #             title="Help Menu",
        #             input_message_content=content,
        #             description="Help for command",
        #             reply_markup=InlineKeyboardMarkup(help_menu(0, ASSISTANT_HELP, "help")),
        # )],
        # cache_time=1)


blocked =[]
def blocked_user(name):
    blocked.append(name)

    
@bot.on_message(filters.command(["alive"]) & filters.group & filters.incoming)
async def alive(client, message):

       cap = f"""
**υѕєявσт ιѕ αℓινє!
**Owner**‌-: __{OWNER}__
**Time**: __{time}__
**Commands**: __{ttl}__
**Ping**: __12__
**Updates**: __{updates}__
**Self Hosted**: __{self_hosted}__
**Mode**: __{MODE}__
**"""

       wh = [
            [
                InlineKeyboardButton(
                    text="Help Menu", callback_data="sed_help_{}".format(message.chat.id)
                )
            ],
        ]
       await bot.send_document(message.chat.id, ALIVE_IMG_ASSISTANT, caption = cap ,
       reply_markup=InlineKeyboardMarkup(wh))
 




@bot.on_callback_query(filters.regex(pattern="sed_help_(.*)"))

async def detailed(client, query):
    o = query.matches[0].group(1)

    await bot.send_document(o ,document=ALIVE_IMG_ASSISTANT, caption="ASSISTANT HELP MENU", reply_markup=InlineKeyboardMarkup(help_menu(0, ASSISTANT_LIST, "help", alive = False)))


@bot.on_callback_query(filters.regex(pattern="help_next\((.+?)\)"))
@inline_help_wrapprs
async def query_hndr(client, message):
    b=await app.get_me()
    if message.from_user.id  == b.id:  # pylint:disable=E0602
        client_page = int(message.matches[0].group(1))
        reply_markup = help_menu(
            client_page + 1, LIST, "help"  # pylint:disable=E0602
        )
        await message.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(reply_markup))
    else:
      
        client_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"

        await message.answer(client_is_best, cache_time=0, show_alert=True)


            # Thanks To Friday For This Deatiled Idea of detail button
@bot.on_callback_query(filters.regex(pattern="detailed_(.*)(assistant|normal)"))

async def detailed(client, message):

    light_pulu_name = message.matches[0].group(1)
    typea = message.matches[0].group(2)
    aa = f"{light_pulu_name}'s help"
    try:
            if light_pulu_name in COMMAND_HELP:
                    lightning_help_strin = f"{language('Commands found in')} {light_pulu_name}:\n"
                    lightning_help_strin += f"**🔺 NAME 🔺 :** {light_pulu_name} \n\n {COMMAND_HELP[aa]}"
                    lightning_help_strin += "\n    " + light_pulu_name
                    lightning_help_strin += "\n"
                    o  =  [
            [
                InlineKeyboardButton(
                    text="Delete", callback_data=f"krish_{light_pulu_name}"
                )
            ],
            [
             InlineKeyboardButton(
                    text="Back", callback_data=f"back_{light_pulu_name}{typea}"
                )
            ],
        ]
                    await message.edit_message_text(
                    text=lightning_help_strin,
                    reply_markup=InlineKeyboardMarkup(o)
                
        )
            else:
                await message.answer(f"{language('No Deatiled Help For Command')} {light_pulu_name}", cache_time=0, show_alert=True)
    
     
                

              
        
    except KeyError:
           await message.answer(f"{language('No Details')} U_U", cache_time=0, show_alert=True)
    
 
                
@bot.on_callback_query(filters.regex(pattern="lightning_plugins_(.*)(assistant|normal)"))


async def query_hndr(client, message):
        a = 0
        me = await app.get_me()
        if not  message.from_user.id ==  me.id:
               await message.answer("OwO, U cannot use anything.")
        else:

           light_pulu_name = message.matches[0].group(1)
           type_ = message.matches[0].group(2)
           pg_no = message.matches[0].group(1)
        # if light_pulu_name in  str(COMMAND_HELP[light_pulu_name]):
           
           hlp_str  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n{COMMAND_HELP[light_pulu_name]}"
           
           hlp_str += "\n\n**In Case Any Problem @lightning_support_grup** ".format(light_pulu_name)
           mkp = [
            [
                InlineKeyboardButton(
                    text="Details", callback_data=f"detailed_{pg_no}{type_}"
                )
            ],
            [
             InlineKeyboardButton(
                    text="Back", callback_data=f"back_{a}{type_}"
                )
            ],
        ]
         
    
    
           await message.edit_message_text(
             hlp_str,
            reply_markup=InlineKeyboardMarkup(mkp)
           )
@bot.on_callback_query(filters.regex(pattern="help_prev\((.+?)\)"))

async def query_hndr(client, message): 
    me = await app.get_me()
    if not  message.from_user.id ==  me.id:
               await message.answer("I said you cannot use anything. ఠ_ఠ", show_alert=True)
    else:

        lightning_page = int(message.matches[0].group(1))
        reply_markup = help_menu(
             lightning_page - 1, LIST, "help"  # pylint:disable=E0602
        )
        await message.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(reply_markup))




@bot.on_callback_query(filters.regex(pattern="lightning_is_here_cant_spam"))
@owner
async def lightning_is_better(client, message):

    user = await app.get_users(int(message.chat.id))
    text1 = f"**Byy👋**!\n**You've been blocked have fun\n\n**If you think this is a mistake contact master via {g}**"
    app.block_user(user.id)
    blocked_user(user.first_name)
    await app.send_message(message.chat.id, text1)


urgent = []




def add_friend(name, id):
    Friends.update({name: id})
def add_urgent(name):
    urgent.append(name)



@bot.on_callback_query(filters.regex(pattern="urgent"))
async def lightning_is_better(client, message):
    a = await app.get_me()
    user = await app.get_users(int(message.chat.id))

    if user.is_self :
        await message.answer("This command if for stranger not for the owner!", cache_time=0, show_alert=True)
        return

    name = user.first_name
    bhat = user.status  
    text1 = "**Hello User {},  master was last online on {}**\n**Kindly wait for him to be online :)** ".format(name, bhat)
    await app.send_message(message.chat.id, text1)
    await app.send_message(
        Variable.LOGS_chat.id,
        f"**Hello {USER}, [{name}]({user.id}) wants to dicuss something important!.**",
    )
    if user.is_deleted:
     return
    add_urgent(name)






@bot.on_callback_query(filters.regex(pattern="he_sucks"))
@owner
async def lightning_is_better(client, message):
    user =   await app.get_users(int(message.chat.id))
    o = await app.get_me()
    owner = await app.get_users(int(o.id

    ))
    user_id = user.id
    await message.edit(f"**Hello {user.first_name} if u are friend kindly contact him via {g}**\n\n__{USER}:- was last online on__ {owner.last_online_date}")

    
    
    
    
    
    




@bot.on_callback_query(filters.regex(pattern="fck_ask"))
@owner
async def lightning_is_better(client, message):
    user =   await app.get_users(int(message.chat.id))
    bot_id = await bot.get_me()
    bot_id = bot_id.id
    await message.edit
    btn =InlineKeyboardMarkup([InlineKeyboardButton("Contact Him", url=f"tg://user?id={bot_id}")])

    await app.send_message(
        user.id,
        f"Master is busy for some reason contact him via bot link given below",
        reply_markup=btn,
    )


          




@bot.on_callback_query(filters.regex(pattern="krish_(.*)"))
async def chill(client, message):

    file=message.matches[0].group(1)
    pg_no=message.matches[0].group(1)
    a = 0
    await message.edit_message_text(
            f"`File and plugin Removed`",
            reply_markup=InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Ⴆαƈƙ 💢", callback_data="back_{}".format(a))],

        ],)
    )
    os.remove('system/plugins/' + file + ".py" )
    logging.info("REMOVED:- {}".format(file))
    
# Thanks To Friday Userbot and @Midhun_xD For This idea







@bot.on_callback_query(filters.regex(pattern="back_(.*)(assitant|normal)"))
async def ho(client, message):
    o=message.matches[0].group(1)
    if message.matches[0].group(2) == "assistant":
     sv = ASSISTANT_LIST
    else:
     sv = LIST
    await message.answer("Returned To Home", cache_time=0, show_alert=False)
    reply_markup = help_menu(o, sv, "help")
    ho = f"""**Black Lightning {language('help menu')}**: {language('Commands')}: {len(sv)}"""
    await message.edit_message_text(ho, reply_markup=InlineKeyboardMarkup(reply_markup))





        



def help_menu(pg_num, setv, prefix, alive: bool =  False):
    number_of_rows = 6
    number_of_cols = 2

    sortsed = []
    if alive:
        data = "_cmd_data_"
        help = "_preve"
        help2 = "_nexte"
        type_ = "assistant"
    else:
        help = "_prev"
        help2 = "_next"
        type_ = "normal"
        data = f"lightning_plugins_"
    for p in setv:
        a = p.replace(".py", "")
        if not p.startswith("_"):
            sortsed.append(a)
    sortsed = sorted(sortsed)
    modules = [  
        InlineKeyboardButton(
            text=f"X {x} X",
            callback_data=f"{data}{x}{type_}"
        )
        for x in sortsed 
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    pg_num = 0 % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            pg_num * number_of_rows : number_of_rows * (pg_num + 1)
        ] + [
            (
                InlineKeyboardButton(
                    text="Previous",
                    callback_data="{}{}({})".format(prefix,help, pg_num)
                ),
                InlineKeyboardButton(
                    text="Next",
                    callback_data="{}_next({})".format(
                        prefix, help2, pg_num
                    ),
                ),
            )
        ]
    return pairs


@bot.on_message(filters.command(["Commands"]) & filters.incoming)
async def command(client ,event):
    for i in ASSISTANT_HELP:
        if i.startswith('_'):
            return
        plugs.append(i)
    des = sorted(plugs)
    
    buttons = help_menu(0, ASSISTANT_HELP, 'help')
    if des in ASSISTANT_HELP:

     await event.edit_message_reply_markup(reply_markup =buttons)

@bot.on_callback_query(filters.regex(pattern="_cmd_data_(.*)"))

async def lightning_pugins_query_hndlr(client ,event):
    command = ASSISTANT_HELP['Command']
    cmd = event.matches[0].group(1)
    type = ASSISTANT_HELP[f"{cmd}'s Type"]
    try:
    
     if cmd in ASSISTANT_HELP:
        assistant_help_strin = f"**✡ Type : {type} ✡**"
        assistant_help_strin  += f"**🔺 COMMAND 🔺 :** `{cmd}` \n\n{command}"
        
        assistant_buttons = assistant_help_strin 
        assistant_buttons += "\n\n**In Case Any Problem @lightning_support_grup**".format(cmd)
        await event.edit_message_text(assistant_buttons)
    
    except KeyError:
        await event.answer("The command isn't displayable", cache_time=0, alert=True)


@bot.on_callback_query(filters.regex(pattern="help_preve\((.+?)\)"))

async def lightning_pugins_query_hndlr(client, lightning):
        me = await app.get_me()
        if not  message.from_user.id ==  me.id:
               await message.answer("I said you cannot use anything. ఠ_ఠ", show_alert=True)
        else:
            lightning_page = int(lightning.matches[0].group(1))
            buttons = help_menu(
                lightning_page - 1, ASSISTANT_HELP, "help"  # pylint:disable=E0602
            )
            await lightning.edit_message_reply_markup(reply_markup=buttons)

import io
# from system.sqls.bot_sql import *

# @bot.on_callback_query(filters.regex(pattern="users"))


# async def d(client ,message):
#     with io.BytesIO(str.encode(get_ids())) as out_file:
#         out_file.name = "cmd_list.txt"
#     await bot.send_document(message.chat.id, document=out_file)

@bot.on_callback_query(filters.regex(pattern="help_nexte\((.+?)\)"))
  
async def ass_pugins_query_hndlr(client, lightning):
        await lightning.delete()
        lightning_page = int(lightning.matches[0].group(1))
        
        buttons = help_menu(
            lightning_page + 1, ASSISTANT_HELP, "help"  # pylint:disable=E0602
        )
        await lightning.edit_message_reply_markup(reply_markup=buttons)





