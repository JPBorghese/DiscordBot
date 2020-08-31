
import discord, sys, re
from commands import *

if len(sys.argv) != 2 :
    print('python bot.py <TOKEN.txt>')
    sys.exit(1)

client = discord.Client()

@client.event
async def on_message(message):
    print(message.author.display_name + ":\n\t" + message.content)

    #commands
    if (message.content.startswith('$')):
        command = message.content[1:len(message.content):1]
        if(re.match("^[a-zA-Z_]+$", command)):
            try:
                await eval(command + '.' + command + '(message)')
            except:
                pass
        else:
            print('invalid command : ' + command)
    #text
    elif (message.content.startswith('!')):
        command = message.content[1:len(message.content):1]
        if(re.match("^[a-zA-Z_]+$", command)):
            try:
                await message.delete()
                f = open('pasta/' + command + '.txt', 'r', encoding='utf-8')
                await message.channel.send(f.read())
                f.close()
            except:
                pass

@client.event
async def on_reaction_add(reaction, user):
    if (reaction.message.channel.id == 749388765717332019):
        await reaction.message.channel.send(reaction.emoji)

client.run(open(sys.argv[1], 'r').read())
