#! bin/bash

# Copyright (C) 2021 KeinShin@Github.

count=0
for f in system/plugins/*.py
do 

   python "$f"
   echo "LOADDED -  " +  $f
   count+=1
done
