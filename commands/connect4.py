
import discord

data = []

async def connect4(message, client):
    width = 7
    height = 6
    empty = ":white_circle:"
    full = ":red_circle:"

    arr = [[0 for x in range(width)] for y in range(height)]

    embed = discord.Embed(
        title = "Connect Four",
        color = 0xff9933,
        description = "its your turn!!"
    )

    board = ""
    for y in range(height):
        for x in range(width):
            board += empty
        board += "\n"
    board += ":one::two::three::four::five::six::seven:"

    embed.add_field(name="asdf", value=board, inline=False)

    msg = await message.channel.send(embed=embed)

    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")
    await msg.add_reaction("3️⃣")
    await msg.add_reaction("4️⃣")
    await msg.add_reaction("5️⃣")
    await msg.add_reaction("6️⃣")
    await msg.add_reaction("7️⃣")
