from discord.ext import commands
import requests
import sys
sys.path.insert(1, '../')
from config import *

class anek(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True)
    async def anek(self, ctx):
        try:
            r = requests.get('https://baneks.ru/random')
            r.encoding = 'utf-8'
            
            text  = scrap(r.text, "article")
            title = scrap(text, "h2")
            anek  = scrap(text, "p")

            anek = anek.replace("<br />", "")

            await ctx.send("**" + title + "**\n" + anek)
        except Exception:
            await ctx.send('Unable to get anek')

#
def setup(bot):
    bot.add_cog(anek(bot))

def scrap(text, element):
    start = text.find('<' + element + '>') + len('<' + element + '>')
    end = text.find('</' + element + '>') - start
    result = text[start:start + end]

    return result