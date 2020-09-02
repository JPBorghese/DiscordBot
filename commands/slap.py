

async def slap(message, client):
    messageArray = message.content.split()

    #check more than 1 'token'
    if len(messageArray) == 2:
        mentions = message.mentions

        #format output string
        if len(mentions) > 0:
            botMessage = message.author.mention + " slapped"
            for i in range(len(mentions)):
                if len(mentions) == 1:
                    botMessage += " "
                elif i == len(mentions) - 1:
                    botMessage += " and "
                elif i != 0:
                    botMessage += ", "

            botMessage += mentions[i].mention + " in the face!"

            await message.channel.send(botMessage)

