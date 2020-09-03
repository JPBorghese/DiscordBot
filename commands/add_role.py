
async def add_role(message, client):

    #check if there are at least 2 'tokens' in command
    if len(message.content.split()) > 1:
        newRole = message.content.split()[1]
        roles = message.channel.guild.roles

        added = False

        #check if role exists
        for role in roles:
            if role.name == newRole:
                if role.permissions.value == 0:
                    await message.author.add_roles(role)
                    added = True
                    break
                else:
                    await message.channel.send("You can only add roles without permissions")

        #send error message if failed
        if not added:
            await message.channel.send("Invalid Role: " + newRole)