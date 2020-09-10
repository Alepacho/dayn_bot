import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import MissingPermissions
from discord.ext.commands import NotOwner
from config import *

bot = commands.Bot(command_prefix = 'danik ')

@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Game(name = "type 'danik help'"))

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return
	if isinstance(error, NotOwner):
		await ctx.send('sosi')
		return
	
	raise error

@bot.command()
@commands.is_owner()
async def die(ctx):
	await ctx.send('rip')
	await ctx.bot.logout()

#bot.load_extension("cogs.foo")
bot.load_extension("cogs.roll")
bot.load_extension("cogs.say")
#bot.load_extension("cogs.magik")
bot.load_extension("cogs.image")
bot.load_extension("cogs.anek")

bot.run(DISCORD_TOKEN)
