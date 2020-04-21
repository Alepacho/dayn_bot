import sys
import discord
from discord.ext import commands

from config import *
#
#

# passing tokens though args
DISCORD_TOKEN = sys.argv[1]
RANDOM_TOKEN  = sys.argv[2]

bot = commands.Bot(command_prefix = 'greg ')

@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Game(name = "'greg '"))
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
@commands.is_owner()
async def die(ctx):
	await ctx.send('rip')
	await ctx.bot.logout()

bot.load_extension("cogs.foo")
bot.load_extension("cogs.roll")

bot.run(DISCORD_TOKEN)
