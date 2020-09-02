
async def add_role(stuff):

    #check if there are at least 2 'tokens' in command
    if len(stuff["message"].content.split()) > 1:
        newRole = stuff["message"].content.split()[1]
        roles = stuff["message"].channel.guild.roles
        added = False

        for role in roles:
            if role.name == newRole:
                await stuff["message"].author.add_roles(role)
                added = True
                break

        if not added:
            await stuff["message"].channel.send("Invalid Role: " + newRole)