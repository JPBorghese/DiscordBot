
async def remove_role(stuff):

    #check if there are at least 2 'tokens' in command
    if len(stuff["message"].content.split()) > 1:
        newRole = stuff["message"].content.split()[1]
        roles = stuff["message"].channel.guild.roles

        for role in roles:
            if role.name == newRole:
                await stuff["message"].author.remove_roles(role)
                break