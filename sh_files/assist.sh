#! bin/bash
# Copyright (C) 2021 KeinShin@Github.

count=0
for f in system/user_bot_assistant/*.py
do 
   echo "Loading assistant!"
   python "$f"
   echo "LOADDED -  " +  $f
   count+=1
done
