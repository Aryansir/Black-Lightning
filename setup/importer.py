# Copyright (C) 2021 KeinShin@Github.


import logging
import os
import importlib
from system import app


class Start:
    def __init__(self, name: str):
        self.name = name
        path = self.name.split("/")
        self.path = ".".join(path)
        
        self.x= [x for x in os.listdir(self.name) if x.endswith(".py") and not x.startswith("__")]    
    

    def boot(self):
          for i in self.x:
              a=f"{self.path}{i.replace('.py', '')}"
              importlib.import_module(a)
              logging.info(f"IMPORTED - {i}")
