import sys
import discord
#from commands import *
import rndapi
from discord.ext import commands

# passing token though args
token = sys.argv[1]

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
	result = rndapi.get(max)
	await ctx.send('Result: {_result}'.format(_result = result))

@bot.command()
@commands.is_owner()
async def die(ctx):
	await ctx.send('rip')
	await ctx.bot.logout()


bot.run(token)
