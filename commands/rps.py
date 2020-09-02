
# made by RobertBorghese

import discord

has_reaction_callback = False

running_data = []

async def rps(message, client):
	global running_ids
	global has_reaction_callback
	if has_reaction_callback == False:
		@client.event
		async def on_reaction_add(reaction, user):
			if reaction.message.author.id == client.user.id:
				for data in running_data:
					if data[0] == reaction.message.id:
						if data[1] == user.id:
							other_type = None
							if reaction.emoji == "🌚":
								other_type = "🌚"
							elif reaction.emoji == "📰":
								other_type = "📰"
							elif reaction.emoji == "✂":
								other_type = "✂"
							else:
								return

							running_data.remove(data)

							original_type = data[3]

							embed = discord.Embed(
								title = "Rock, Paper, Scissors!",
								color = 0xff9933,
								description = ""
							)

							embed.add_field(name=data[4], value=other_type, inline=True)
							embed.add_field(name="VS.", value="---", inline=True)
							embed.add_field(name=data[5], value=original_type, inline=True)

							quote = "\"Get rekt noob.\""

							if other_type == original_type:
								final_message = ("It is a tie.")
								quote = "\"You are both stupid noobs.\""
							elif (other_type == "🌚" and original_type == "✂") or (other_type == "✂" and original_type == "📰") or (other_type == "📰" and original_type == "🌚"):
								final_message = (data[4] + " won!")
							elif (original_type == "🌚" and other_type == "✂") or (original_type == "✂" and other_type == "📰") or (original_type == "📰" and other_type == "🌚"):
								final_message = (data[5] + " won!")

							embed.add_field(name=final_message, value=quote, inline=False)

							msg = await channel.send(embed=embed)

						break
		has_reaction_callback = True

	if message.content.startswith("$rps"):
		if len(message.mentions) < 1:
			await message.channel.send("Mention a user to challenge!")
			return

		mentioned_user = message.mentions[0]

		await message.delete()

		channel = message.channel
		content = message.content

		type = None
		stuff = content.split()
		if "rock" in stuff:
			type = "🌚"
		elif "paper" in stuff:
			type = "📰"
		elif "scissors" in stuff:
			type = "✂"
		else:
			await channel.send("Please include either rock, paper, or scissors in your message!")
			return


		embed = discord.Embed(
			title = "Rock, Paper, Scissors!",
			color = 0xff9933,
			description = ("" + message.author.mention + " has challenged " + mentioned_user.mention + "!\nWhat move will you choose " + mentioned_user.mention + "?")
		)

		msg = await channel.send(embed=embed)

		running_data.append((msg.id, mentioned_user.id, message.author.id, type, mentioned_user.display_name, message.author.display_name))

		await msg.add_reaction("🌚")
		await msg.add_reaction("📰")
		await msg.add_reaction("✂")