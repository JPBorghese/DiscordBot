
#⚪🔴🔵
#add custom board size

import discord

data = []
first = False

async def on_reaction_add(reaction, user):
    global data

    for d in data:
        #check if the correct person reacted
        if user.id == d[1][d[2]]:
            #check that the reaction is for the correct board
            if d[0] == reaction.message.id:

                reactID = ord(reaction.emoji[0]) - 49

                boardChanged = False

                #find first y thats not 0
                for y in range(d[5] - 1, 0, -1):
                    if d[3][reactID][y] == 0:
                        d[3][reactID][y] = 1
                        boardChanged = True
                        break

                #change whose turn it is
                if boardChanged:
                    d[2] += 1
                    if d[2] >= len(d[1]):
                        d[2] = 0

                embed = discord.Embed(
                    title = "Connect Four",
                    color = 0xff9933,
                    description = getStringArray(d[3], d[4], d[5])  + "\n\n **Current Turn:** " + d[7][d[2]]
                )

                await reaction.message.edit(embed=embed)

#edit the embed

def getStringArray(arr, w, h):
    empty = "⚪"
    red = "🔴"
    blue = "🔵"

    board = ""
    for y in range(h):
        for x in range(w):
            if arr[x][y] == 0:
                board += empty
            else:
                board += red
        board += "\n"
    board += ":one::two::three::four::five::six::seven:"

    return board

async def connect4(message, client):

    if not first:
        firsr = True
        client.event(on_reaction_add)

    #width <= 10
    width = 7
    #height <= 12
    height = 6

    arr = [[0 for y in range(height)] for x in range(width)]

    embed = discord.Embed(
        title = "Connect Four",
        color = 0xff9933,
        description = getStringArray(arr, width, height) + "\n\n **Current Turn:** " + message.author.display_name
    )

    msg = await message.channel.send(embed=embed)

    players = [message.author.id, message.mentions[0].id]
    names = [message.author.display_name, message.mentions[0].display_name]
    whoseTurn = 0

    data.append([msg.id, players, whoseTurn, arr, width, height, client.user.id, names])

    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")
    await msg.add_reaction("3️⃣")
    await msg.add_reaction("4️⃣")
    await msg.add_reaction("5️⃣")
    await msg.add_reaction("6️⃣")
    await msg.add_reaction("7️⃣")

