import discord

#prints possible roles to add
async def roles(message, client):
    roles = message.guild.roles

    botOut = ""
    for r in roles:
        botOut += r.name + "\n"

    embed = discord.Embed(
        title = "Roles:",
        color = 0xff9933,
        description = botOut
    )

    await message.channel.send(embed=embed)