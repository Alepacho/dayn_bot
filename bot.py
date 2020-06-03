import discord
from discord.ext import commands

from config import *

bot = commands.Bot(command_prefix = 'greg ')

@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Game(name = "'greg '"))

#@bot.command()
#@commands.is_owner()
#async def die(ctx):
#	await ctx.send('rip')
#	await ctx.bot.logout()

#bot.load_extension("cogs.foo")
bot.load_extension("cogs.roll")
bot.load_extension("cogs.say")
bot.load_extension("cogs.magik")
bot.load_extension("cogs.image")

bot.run(DISCORD_TOKEN)
