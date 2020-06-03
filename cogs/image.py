from discord.ext import commands

import wand                         # make magic
import requests                     # download file
from os.path import splitext        # getting file extension
from urllib.parse import urlparse   #

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
            r = requests.get(url, stream = True)
        except Exception:
            await ctx.send('Unable to download file.')
            return
        
        ext = splitext(urlparse(url).path)[1]

        if not valid_format(ext):
            await ctx.send('Unsupported file format.')
            return
        
        await ctx.send('Processing...')

        file_name_raw = 'gray_raw{}'.format(ext)
        file_name_rst = 'gray{}'.format(ext)

        # saving raw
        with open(file_name_raw, 'wb') as img:
            img.write(r.content)
        del r

        # making it gray (wow)
        with wand.image.Image(filename = file_name_raw) as img:
            img.type = 'grayscale'
            img.save(filename = file_name_rst)
        
        # send the result
        await ctx.send(file = discord.File(file_name_rst))

#
def setup(bot):
    bot.add_cog(image(bot))

