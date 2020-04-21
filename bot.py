import sys
import discord
#from commands import *
import rndapi
from discord.ext import commands

# passing tokens though args
discord_token = sys.argv[1]
random_token  = sys.argv[2]

bot = commands.Bot(command_prefix = 'greg ')

#
@bot.command()
async def ping(ctx):
	await ctx.send('pong')

@bot.command()
async def say(ctx, *msg):
	text = ' '.join(msg)
	await ctx.message.delete()
	await ctx.send(text)

@bot.command()
async def roll(ctx, max = 100):
	result = rndapi.get(random_token, max)
	await ctx.send('Result: {_result}'.format(_result = result))

@bot.command()
@commands.is_owner()
async def die(ctx):
	await ctx.send('rip')
	await ctx.bot.logout()


bot.run(discord_token)
