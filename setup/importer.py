# Copyright (C) 2021 KeinShin@Github.


import logging
import os
import importlib

class Start:
    def __init__(self, name: str):
        self.name = name
        path = self.name.split("/")
        self.path = ".".join(path)
        
        self.x= [x for x in os.listdir(self.name) if x.endswith(".py") and not x.startswith("__")]    

    

    def start(self):
          for i in self.x:
              importlib.import_module(f"{self.path}{i}")
              logging.info(f"IMPORTED - {i}")
