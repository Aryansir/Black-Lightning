## Way to create your plug by fork

``` 
from system.decorators import on_cmd 
from system import *
from system.Config import Variable

@on_cmd(["xyz plug", sudo=True ( if you want sudo access ), sudo_ids=Variable.SUDO_IDS ( if sudo is true else leave both)])
async def command(client, message):
   await message.reply("Hello Sur!)
   
```

# BTW having basic knowledege of python will be fruitfull else you will be confused XoX  


## Thats it folks!
