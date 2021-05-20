# Copyright (C) 2021 KeinShin@Github.


import logging
import os
import importlib
import pyrogram


class Start:
    def __init__(self, name: str):
        self.name = name
        path = self.name.split("/")
        self.path = ".".join(path)
        self.pat  = None
        self.x= [x for x in os.listdir(self.name) if x.endswith(".py") and not x.startswith("__") ]    
    

    def boot(self):
          
        a=f"{self.path}"
        return    importlib.import_module(f"{a}{self.pat}")
