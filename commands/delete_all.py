
async def delete_all(message, client):

    if message.author.id == 265342981597429761:
        #loop through all messages
        async for message in message.channel.history(limit=200):
            try:
                await message.delete(delay = .01)
            except:
                pass
    else:
        await message.channel.send("$delete_all is too powerful")