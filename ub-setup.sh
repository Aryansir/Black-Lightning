#!/bin/bash

# Copyright (C) 2021 KeinShin@Github.
path = "sh_files/load.sh"
path2 = "sh_files/assist.sh"

if [ -e exconfig.py  ]
then
    a="""
LOADING USERBOT  - KINDLY WAIT 5min. 

INITIALIZING - Self Hosting Setup 

© Black-Lightning 2021"""
    


else
    a =     """LOADING USERBOT  - KINDLY WAIT 5min. 

USERBOT -  Black-Lightning

© Black-Lightning 2021"""


fi


echo a





echo "Loading Plugins"
bash "$path"







echo "Loading Assistant"
bash "$path2"
