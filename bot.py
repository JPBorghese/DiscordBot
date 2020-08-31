
import discord, sys
from commands import *

if len(sys.argv) != 2 :
    print('python bot.py <TOKEN.txt>')
    sys.exit(1)

client = discord.Client()

@client.event
async def on_message(message):
    print(message.author.display_name + ":\n\t" + message.content)
    if (message.content.startswith('$')):
        command = message.content[1:len(message.content):1]
        try:
            await eval(command + '.' + command + '(message)')
            print(command + '.' + commnad + '(message)')
        except:
            pass

@client.event
async def on_reaction_add(reaction, user):
    if (reaction.message.channel.id == 749388765717332019):
        await reaction.message.channel.send(reaction.emoji)

client.run(open(sys.argv[1], 'r').read())
