import discord, asyncio, time
from discord.ext.commands import Bot
from discord.ext import commands


token = input("Enter Bot's Token\n")
prefix_real = "Greg"
prefix = prefix_real.upper()

d_client = discord.Client()
client = commands.Bot(command_prefix = prefix)

def command(message, cmd):
	if message.content.upper().startswith(prefix + " " + cmd):
		print(message.author.name + ": " + message.content)
		return True
	else:
		return False

@client.event
async def on_ready():
	print("Bot just connected!")
	await client.change_presence(game = discord.Game(name = "Use '" + prefix_real + " help'"))
	print(client.get_all_members())
	
@client.event
async def on_message(message):
	if command(message, "PING"):
		await client.send_message(message.channel, "pong")
		
	if command(message, "HELP"):
		l_a = message.author
		l_text = "### HELP LIST ###\nPrefix: " + prefix_real + "\n\n### COMMANDS ###\nSay [Text] - repeat your text.\nPing - write pong"
		await client.send_message(l_a, l_text)
		
	if command(message, "CNAME"):
		if len(message.content) > len(prefix + " CNAME"):
			l_split = message.content.split(" ")
			
			#print(client.display_name)
			#await d_client.change_nickname(d_client, " ".join(l_split[2:]))
			await client.send_message(message.channel, "done")
		else:
			await client.send_message(message.channel, "i can't, faggot")
			
	if command(message, "SAY"):
		if message.author == client.user:
			return
		if len(message.content) > len(prefix + " SAY"):
			l_split = message.content.split(" ")
			await client.send_message(message.channel, "%s" %(" ".join(l_split[2:])))
		else:
			await client.send_message(message.channel, "don't be a dick")
	#message.author.id ==

client.run(token)
