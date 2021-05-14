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

git clone https://github.com/KeinShin/Black-Lightning -b rebirthed 
cd Desktop

chmod +x /usr/local/bin/*
cd Black-Lightning


python3 -m system
