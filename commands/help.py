import discord, os

async def help(message, client):

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

    counter = 0
    wordSpace = 16

    cmds = "**```"
    for x in commandFiles:
        cmds += "$" + x
        counter += 1

        if counter % 2 == 0:
            cmds += '\n'
        else:
            for i in range(wordSpace - len(x)):
                cmds += ' '

    cmds += "```**"

    texts = "**```"
    counter = 0

    for x in textFiles:
        texts += "!" + x
        counter += 1

        if counter % 2 == 0:
            texts += '\n'
        else:
            for i in range(wordSpace - len(x)):
                texts += ' '
    texts += "```**"

    embed = discord.Embed(
      title = "$Help",
      color = 0xff9933,
      description = "",
      #type = "rich"
    )

    embed.add_field(name="🍝 Pasta 🍝", value=texts, inline=True)
    embed.add_field(name="🤖 Commands 🤖", value=cmds, inline=True)
    #embed.add_field(name="Field Name", value="Field content!!!", inline=True)

    await message.channel.send(embed=embed)
