
async def delete_all(message):
    if message.channel.id == 749388765717332019:
        async for message in message.channel.history(limit=200):
            try:
                await message.delete()
            except:
                pass