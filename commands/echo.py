
async def echo(stuff):
    messageArray = stuff["message"].content.split()
    if len(messageArray) > 1:
        botMessage = ""

        for x in range(1, len(messageArray)):
            botMessage += messageArray[x] + " "

        await stuff["message"].channel.send(botMessage)