
async def echo(message, client):
    messageArray = message.content.split()
    #check if more than 1 'token'
    if len(messageArray) > 1:
        botMessage = ""

        #print all except first elemtn in array
        for x in range(1, len(messageArray)):
            botMessage += messageArray[x] + " "

        await message.channel.send(botMessage)