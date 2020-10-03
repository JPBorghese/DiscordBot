
async def removerole(message, client):

    #check if there are at least 2 'tokens' in command
    if len(message.content.split()) > 1:
        newRole = message.content.split()[1].lower()
        roles = message.channel.guild.roles

        for i in range(len(roles)):
            roles[i].name = roles[i].name.lower();

        deleted = False

        #check if role exists
        for role in roles:
            if role.name == newRole:
                await message.author.remove_roles(role)
                deleted = True
                break

        #send error message if failed
        if not deleted:
            await message.channel.send("Invalid Role: " + newRole)