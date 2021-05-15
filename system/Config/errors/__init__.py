# Copyright (C) 2021 KeinShin@Github.



class invalidString(Exception):
    def __init__(self, message):
          self.message = message
class HNDLRERROR(Exception):
    def __init__(self, message):
        self.message = message
        

class BotTokenError(Exception):
    def __init__(self, message):
        self.message = message


