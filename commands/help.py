import discord

async def help(stuff):

    counter = 0
    wordSpace = 16

    cmds = "**```"
    for x in stuff["commandFiles"]:
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

    for x in stuff["textFiles"]:
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

    embed.add_field(name="Pasta", value=texts, inline=True)
    embed.add_field(name="Commands", value=cmds, inline=True)
    #embed.add_field(name="Field Name", value="Field content!!!", inline=True)

    await stuff["message"].channel.send(embed=embed)
