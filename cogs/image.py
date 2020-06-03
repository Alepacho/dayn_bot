from discord.ext import commands

import wand                         # make magic
import requests                     # download file
import os, urlparse                 # getting file extension

def valid_format(_ext):
    vf_list = {
        '.jpg': True,
        '.png': True,
        '.gif': True
    }

    return vf_list.get(_ext, False)

class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def gray(self, ctx, url):
        try:
            r = requests.get(url, stream=True)
        except Exception:
            await ctx.send('Unable to download file.')

        parsed = urlparse(url)
        file_name, ext = splitext(parsed.path)

        if not valid_format(ext):
            except await ctx.send('Unsupported file format.')

        
        await ctx.send('Processing {}...'.format(ext))
        #with open('magik_original.png', 'wb') as img:
        #    img.write(response.content)
        #del response

        #with Image(filename='color.jpg') as img:

#
def setup(bot):
    bot.add_cog(image(bot))

