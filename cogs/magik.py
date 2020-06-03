#has some NotSoBot code fragments
from io import BytesIO
import wand, wand.color, wand.drawing
#import PIL, PIL.Image, PIL.ImageFont, PIL.ImageOps, PIL.ImageDraw
import requests
from discord.ext import commands

class magik(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def magik(self, ctx, scale, url):
        scale = float(scale)
        
        response = requests.get(url, stream=True)
        #img = PIL.Image.open(BytesIO(response.content))
        with open('magik_original.png', 'wb') as img:
            img.write(response.content)
        del response

        with wand.image.Image(filename='magik_original.png') as data:
            await ctx.send('workin...')
            #data = wand.image.Image(filename = img.load())
            data.format = 'PNG'

            w1 = int(data.width * 0.5)
            w2 = int(data.width * 1.5)

            h1 = int(data.height * 0.5)
            h2 = int(data.height * 1.5)

            print('scale')
            print(scale)
            d1 = int(0.5 * scale) if scale else 1
            d2 = scale            if scale else 2

            data.liquid_rescale(width=w1, height=h1, delta_x=d1, rigidity=0)
            data.liquid_rescale(width=w2, height=h2, delta_x=d2, rigidity=0)

            data.save(filename = 'magik.png')
            await ctx.send(file = discord.File('magik.png'))
            #except:
            #await ctx.send('failed...')
#
def setup(bot):
    bot.add_cog(magik(bot))
