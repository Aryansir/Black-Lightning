#!/bin/bash

# Copyright (C) 2021 KeinShin@Github.

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
cd Desktop
git clone https://github.com/KeinShin/Black-Lightning -b rebirth


cd Black-Lightning

echo "Installing Requirements"

pip3 install -r requirements.txt && pip3 install --no-cache-dir -r requirements.txt
PATH="$PATH:/usr/local/bin/python
chmod +x /path/to/python/scripts/Black-Lightning/system/*.py 

echo "INITIALIZING System"
python3 -m system
