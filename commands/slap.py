import discord

async def slap(message, client):
    messageArray = message.content.split()

    #check more than 1 'token'
    if len(messageArray) >= 2:
        mentions = message.mentions

        #format output string
        if len(mentions) > 0:
            botMessage = "<@" + str(message.author.id) + "> slapped "

            length = len(mentions)
            commaCount = length - 2
            andCount = 0
            if length >= 2:
                andCount = 1

            for i in range(len(mentions)):
                botMessage += "<@" + str(mentions[i].id) + ">"

                if commaCount > 0:
                    commaCount -= 1
                    botMessage += ", "
                    continue
                elif andCount > 0:
                    andCount -= 1
                    botMessage += " and "
                else:
                    botMessage += " in the face!"

            embed = discord.Embed(
                title = "",
                color = 0xff9933,
                description = botMessage
            )

            await message.channel.send(embed=embed)

