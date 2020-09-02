
async def remove_role(message, client):

    #check if there are at least 2 'tokens' in command
    if len(message.content.split()) > 1:
        newRole = message.content.split()[1]
        roles = message.channel.guild.roles
        deleted = False

        for role in roles:
            if role.name == newRole:
                await message.author.remove_roles(role)
                deleted = True
                break

        if not deleted:
            await message.channel.send("Invalid Role: " + newRole)