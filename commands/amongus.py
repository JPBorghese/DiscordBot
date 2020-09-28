#🤫🎤

import discord, asyncio

among_first = True
among_data = []

async def on_reaction_remove(reaction, user):
    await on_reaction_add(reaction, user)

async def on_reaction_add(reaction, user):
    global among_data

    if reaction.message.author.id != user.id:
        if (reaction.message.id == among_data[0]) and (user.guild_permissions.administrator):
            if reaction.emoji == "🤫":
                await muteAll(among_data[2])
            elif reaction.emoji == "🎤":
                await unmuteAll(among_data[2])


async def muteAll(channel):
    members = channel.members
    await asyncio.wait([person.edit(mute=True) for person in members])

async def unmuteAll(channel):
    members = channel.members
    await asyncio.wait([person.edit(mute=False) for person in members])

async def amongus(message, client):
    global among_first
    global among_data

    if (message.author.voice == None):
        await message.channel.send("Join a voice channel first")
        return

    voiceChannel = message.author.voice.channel

    if among_first:
        among_first = False
        client.event(on_reaction_add)
        client.event(on_reaction_remove)

    embed = discord.Embed(
        title = "Among Us Muter",
        color = 0xff9933,
        description = ""
    )

    msg = await message.channel.send(embed = embed)

    # message, mutedStatus
    among_data = (msg.id, False, voiceChannel)

    await msg.add_reaction("🤫")
    await msg.add_reaction("🎤")