from discord.ext import commands

class foo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def foo(self, ctx):
        await ctx.send('foo')

#
def setup(bot):
    bot.add_cog(foo(bot))

#an example cog
