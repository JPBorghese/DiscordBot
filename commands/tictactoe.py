import discord, math

tic_first = False
tic_data = []

def getEmojiNum(x):
    output = ""
    if x == 1:
        output = "1️⃣"
    elif x == 2:
        output = "2️⃣"
    elif x == 3:
        output = "3️⃣"
    elif x == 4:
        output = "4️⃣"
    elif x == 5:
        output = "5️⃣"
    elif x == 6:
        output = "6️⃣"
    elif x == 7:
        output = "7️⃣"
    elif x == 8:
        output = "8️⃣"
    elif x == 9:
        output = "9️⃣"
    else:
        return "0️⃣"

    return output

def isWin(arr, id):
    temp = 0
    index = 0
    for y in range(3):
        for x in range(3):
            if arr[x][y] == id:
                temp |= 2 ** index
            index += 1
    vals = [0b000000111, 0b000111000, 0b111000000, 0b001001001,  0b010010010, 0b100100100, 0b100010001, 0b001010100]
    for v in vals:
        if (temp & v) == v:
            return True
    return False

def getStringArray(arr):
    ex = '❌'
    oh = '⭕'

    output = ""
    counter = 0
    for y in range(3):
        for x in range(3):
            counter += 1
            if arr[x][y] == -1:
                output += getEmojiNum(counter)
            elif arr[x][y] == 0:
                output += ex
            elif arr[x][y] == 1:
                output += oh

            if x != 2:
                output += "|"
        output += "\n"

    return output

async def on_message_delete(message):
    global tic_data
    for d in tic_data:
        if message.id == d[0]:
            tic_data.remove(d)

async def on_reaction_remove(reaction, user):
    await on_reaction_add(reaction, user)

async def on_reaction_add(reaction, user):
    global tic_data

    #check corrct message and person reacting
    for d in tic_data:
        if user.id == d[1][d[2]]:
            # check reaction is for the corrct message
            if d[0] == reaction.message.id:
                boardChanged = False
                # update array
                posx = (ord(reaction.emoji[0]) - 49) % 3
                posy = math.floor((ord(reaction.emoji[0]) - 49) / 3)

                if d[3][posx][posy] == -1:
                    d[3][posx][posy] = d[2]
                    boardChanged = True

                if boardChanged:
                    currentPlayer = d[2]
                    # change turn
                    d[2] += 1
                    if d[2] >= len(d[1]):
                        d[2] = 0


                    # print the board
                    embed1 = discord.Embed(
                        title = "TicTacToe",
                        color = 0xff9933,
                        description = "<@" + str(d[1][0]) + "> vs <@" + str(d[1][1]) + ">\n\n" + getStringArray(d[3])  + "\n\n **Current Turn:** " + d[5][d[2]]
                    )

                    isDone = False
                    #check if player won
                    if isWin(d[3], currentPlayer):
                        embed2 = discord.Embed(
                            title = "",
                            color = 0xff9933,
                            description = "<@" + str(d[1][d[2]]) + "> wins!"
                        )
                        tic_data.remove(d)
                        isDone = True
                        await reaction.message.channel.send(embed=embed2)
                    await reaction.message.edit(embed=embed1)

                    if isDone:
                        return

async def tictactoe(message, client):
    global tic_first
    if not tic_first:
        tic_first = True
        client.event(on_reaction_add)
        client.event(on_reaction_remove)
        client.event(on_message_delete)

    width = 3
    height = 3

    arr = [[-1 for y in range(height)] for x in range(width)]

    embed = discord.Embed(
        title = "",
        color = 0xff9933,
        description = getStringArray(arr)
    )



    if len(message.mentions) == 0:
        return

    player2 = message.mentions[0]

    players = [message.author.id, player2.id]
    names = [message.author.display_name, player2.display_name]

    msg = await message.channel.send(embed = embed)

    tic_data.append([msg.id, players, 0, arr, client.user.id, names])

    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")
    await msg.add_reaction("3️⃣")
    await msg.add_reaction("4️⃣")
    await msg.add_reaction("5️⃣")
    await msg.add_reaction("6️⃣")
    await msg.add_reaction("7️⃣")
    await msg.add_reaction("8️⃣")
    await msg.add_reaction("9️⃣")


