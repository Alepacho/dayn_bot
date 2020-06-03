import discord
from discord.ext import commands

import wand                         # make magic
import requests                     # download file
from os.path import splitext        # getting file extension
from urllib.parse import urlparse   #
import faces                        # FaceAPP API

def valid_format(_ext):
    vf_list = {
        '.jpg': True,
        '.png': True,
        '.gif': True
    }

    return vf_list.get(_ext, False)

def is_valid_image(_url):
    try:
        r = requests.get(url, stream = True)
    except:
        await ctx.send('Unable to download file.')
        return False
    
    ext = splitext(urlparse(url).path)[1]

    if not valid_format(ext):
        await ctx.send('Unsupported file format.')
        return False
    
    return r

class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    @commands.cooldown(1, 3)
    async def gray(self, ctx, url):
        try:
            r = is_valid_image(url)
        except False:
            return
        
        await ctx.send('Processing...')

        ext = splitext(urlparse(url).path)[1]
        file_name_raw = 'gray_raw{}'.format(ext)
        file_name_rst = 'gray{}'.format(ext)

        # saving raw
        with open(file_name_raw, 'wb') as img:
            img.write(r.content)
        del r

        # making it gray (wow)
        with wand.image.Image(filename = file_name_raw) as img:
            if (img.width < 2048 and img.height < 2048):
                img.type = 'grayscale'
                img.save(filename = file_name_rst)
            else:
                await ctx.send('Too big image.')
                return
        
        # send the result
        await ctx.send(file = discord.File(file_name_rst))

    @commands.command(pass_context = True)
    @commands.cooldown(1, 3)
    async def smile(self, ctx, url):
        try:
            r = is_valid_image(url)
        except False:
            return
        
        await ctx.send('Processing...')
        
        ext = splitext(urlparse(url).path)[1]
        file_name = 'smile{}'.format(ext)

        try:
            img = faces.FaceAppImage(url = url)
        except faces.ImageHasNoFaces:
            await ctx.send('Face is not recognized.')
            return
        except faces.BadImageType:
            await ctx.send('This file is not valid.')
            return
        except faces.BaseFacesException:
            await ctx.send('Unknown error.')
            return
        
        result = img.apply_filter('smile')
        
        await ctx.send(result)

#
def setup(bot):
    bot.add_cog(image(bot))

