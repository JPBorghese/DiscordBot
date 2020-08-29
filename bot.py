
import discord, sys

if len(sys.argv) != 2 :
    print('python bot.py <TOKEN.txt>')
    sys.exit(1)

TOKEN = open(sys.argv[1], 'r').read()

client = discord.Client()

@client.event
async def on_message(message):
    print(message.content)

    if (message.content == "$delete_all" and message.channel.id == 749388765717332019):
        async for message in message.channel.history(limit=200):
            await message.delete()


@client.event
async def on_reaction_add(reaction, user):
    if (reaction.message.channel.id == 749388765717332019):
        await reaction.message.channel.send(reaction.emoji)

client.run(TOKEN)
