
import discord, sys, re, os
from commands import *

if len(sys.argv) != 2 :
    print("python bot.py <TOKEN.txt>")
    sys.exit(1)

client = discord.Client()

textFiles = os.listdir("./pasta")
commandFiles = os.listdir("./commands")
if "__init__.py" in commandFiles:
    del commandFiles[commandFiles.index("__init__.py")]

if "__pycache__" in commandFiles:
    del commandFiles[commandFiles.index("__pycache__")]

for i in range(len(commandFiles)):
    fileName = commandFiles[i]
    commandFiles[i] = fileName[0:len(fileName)-3:1]

for i in range(len(textFiles)):
    fileName = textFiles[i]
    textFiles[i] = fileName[0:len(fileName)-4:1]


@client.event
async def on_message(message):
    print('\t' + message.author.display_name + ":\n" + message.content)

    #commands
    if message.content.startswith("$"):
        command = message.content[1:len(message.content):1]
        if command in commandFiles:
            try:
                await eval(command + '.' + command + "(message)")
            except:
                pass
        else:
            print("invalid command : " + command)
    #text
    elif message.content.startswith('!'):
        command = message.content[1:len(message.content):1]
        if command in textFiles:
            try:
                await message.delete()
                f = open("pasta/" + command + ".txt", 'r', encoding="utf-8")
                await message.channel.send(f.read())
                f.close()
            except:
                pass

@client.event
async def on_reaction_add(reaction, user):
    if (reaction.message.channel.id == 749388765717332019):
        await reaction.message.channel.send(reaction.emoji)

client.run(open(sys.argv[1], 'r').read())
