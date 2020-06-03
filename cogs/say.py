from discord.ext import commands

class say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    @commands.cooldown(1, 1)
    async def say(self, ctx, *msg):
        text = ' '.join(msg)
        await ctx.message.delete()
        await ctx.send(text)

#
def setup(bot):
    bot.add_cog(say(bot))

#an example cog
