from discord.ext import commands

import wand                         # make magic
import requests                     # download file
import os                           # getting file extension

class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def gray(self, ctx, url):
        r = requests.get(url, stream=True)
        ext = os.path.splitext(url)[1]

        if r.getcode() != 200:
            await ctx.send('Unable to download file.')
            return
        
        await ctx.send('Processing {}...'.format(ext))
        #with open('magik_original.png', 'wb') as img:
        #    img.write(response.content)
        #del response

        #with Image(filename='color.jpg') as img:

#
def setup(bot):
    bot.add_cog(image(bot))

