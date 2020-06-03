from discord.ext import commands

class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def gray(self, ctx, url):
        await ctx.send('Got: {}'.format(url))

#
def setup(bot):
    bot.add_cog(image(bot))

