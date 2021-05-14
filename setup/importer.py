# # Copyright (C) 2021 KeinShin@Github.


# from Config.utils import language
# import logging
# # from subprocess import call
# import importlib
# # from importlib import Loader
# import os
# import glob

# class run_py_file:
#     def __init__(self, folder):
#         self.path = folder 
#         # logging.info("Processing Modules")
        
#         # self.file = fille
#     def load(self):
#         # # call([self.path])
#         # o = []
#         # a = []
#         a= [i for i in glob.glob(self.path + "*.py")]
#         #     o.append(i)
#         # # o = []
#         # l=".".join(o)
#         # o=" ".join(o)
#         # # l="."join()
    
#         # o=o.replace(self.path + "\\", "")
#         # o=o.replace(".py", "")
#         # o=o.split()
#         logging.info(f"{language('Processing Modules')}")

#         try:
#             # a= self.path
#             # o = importlib
#             for io in a:
#                 importlib.import_module(io)
#                 logging.info(f"{language('IMPORTED')} - " + io)
#             #  print("Hi" + io)
#         except ModuleNotFoundError as e:
#             a = language("Couldn't load plugins")
#             logging.error("{}: {}".format(a, e))