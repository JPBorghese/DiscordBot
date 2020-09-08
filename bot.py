#help command name
#hangman
import discord, sys, re, os
from commands import *

sys.path.insert(0, '.')

if len(sys.argv) != 2 :
    print("python bot.py <TOKEN.txt>")
    sys.exit(1)

client = discord.Client()

#get all txt and py files
textFiles = os.listdir("./pasta")
commandFiles = os.listdir("./commands")

#remove unwanted file
if "__init__.py" in commandFiles:
    del commandFiles[commandFiles.index("__init__.py")]

if "__pycache__" in commandFiles:
    del commandFiles[commandFiles.index("__pycache__")]

#remove file extensions
for i in range(len(commandFiles)):
    fileName = commandFiles[i]
    commandFiles[i] = fileName[0:len(fileName)-3:1]

for i in range(len(textFiles)):
    fileName = textFiles[i]
    textFiles[i] = fileName[0:len(fileName)-4:1]

#set allowed channels
allowedChannels = [749388765717332019, 751227509168668762]

@client.event
async def on_message(message):
    print('\t' + message.author.display_name + ":\n" + message.content)

    if message.channel.id in allowedChannels and not message.author.bot:

        #commands
        if message.content.startswith("$"):
            command = message.content.split()[0][1:]

            if command in commandFiles:
                await message.delete(delay = .01)
                await eval(command + '.' + command + "(message, client)")
            else:
                print("invalid command : " + command)
        #text
        elif message.content.startswith('!'):
            command = message.content[1:len(message.content):1]
            if command in textFiles:
                await message.delete(delay = .01)
                f = open("pasta/" + command + ".txt", 'r', encoding="utf-8")
                embed = discord.Embed(
                    title="",
                    color = 0xff9933,
                    description = f.read()
                )
                await message.channel.send(embed=embed)
                f.close()

@client.event
async def on_reaction_add(reaction, user):
    if (reaction.message.channel.id == 749388765717332019):
        #await reaction.message.channel.send(reaction.emoji)
        pass

client.run(open(sys.argv[1], 'r').read())
