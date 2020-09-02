
#todo: fix it so that the syntax is, $slap @mention

async def slap(message, client):

    messageArray = message.content.split()
    #check more than 1 'token'
    if len(messageArray) == 2:
        otherName = messageArray[1]

        #find noob's member object
        users = message.guild.members

        otherObject = None
        for i in range(len(users)):
            print(users[i].display_name)
            if otherName == users[i].display_name:
                otherObject = users[i]
                print(otherObject)
                break

        if otherObject != None:
            botMessage = message.author.mention + " slapped "
            botMessage += otherObject.mention + " in the face!"
            await message.channel.send(botMessage)
