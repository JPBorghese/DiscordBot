
async def add_role(message):

    #check if there are at least 2 'tokens' in command
    if len(message.content.split()) > 1:
        newRole = message.content.split()[1]
        roles = message.channel.guild.roles
        added = False

        for role in roles:
            if role.name == newRole:
                await message.author.add_roles(role)
                added = True
                break

        if not added:
            await message.channel.send("Invalid Role: " + newRole)