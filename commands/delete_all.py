
async def delete_all(message, client):
    #loop through all messages
    async for message in message.channel.history(limit=200):
        try:
            await message.delete(delay = .01)
        except:
            pass