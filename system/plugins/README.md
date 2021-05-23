## Way to create your plug by fork

``` 
from system.plugins import light
from system import *
from Config import Variable

@light.on(["xyz plug", sudo_ids=Variable.SUDO_IDS ( if sudo is true else leave both)])
async def command(client, message):
   await message.reply("Hello Sur!)
   
```

# BTW having basic knowledege of python will be fruitfull else you will be confused XoX  


## Thats it folks!