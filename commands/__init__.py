import os

commandFiles = os.listdir("./commands")

if "__init__.py" in commandFiles:
    del commandFiles[commandFiles.index("__init__.py")]

if "__pycache__" in commandFiles:
    del commandFiles[commandFiles.index("__pycache__")]

for i in range(len(commandFiles)):
    fileName = commandFiles[i]
    commandFiles[i] = fileName[0:len(fileName)-3:1]
    
__all__ = commandFiles
