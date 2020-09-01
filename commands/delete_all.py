
async def delete_all(stuff):
    async for message in stuff["message"].channel.history(limit=200):
        try:
            await message.delete(delay = .01)
        except:
            pass