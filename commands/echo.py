
async def echo(message, client):
    messageArray = message.content.split()
    if len(messageArray) > 1:
        botMessage = ""

        for x in range(1, len(messageArray)):
            botMessage += messageArray[x] + " "

        await message.channel.send(botMessage)