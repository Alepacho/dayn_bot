#https://teletype.in/@snakeblog/rJnA9jwEX
import sys
from http.client import HTTPSConnection
from json import dumps, loads
from discord.ext import commands
sys.path.insert(1, '../')
from config import *

class roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def roll(self, ctx, max):
        request_data = {
          'jsonrpc': '2.0',
          'method': 'generateIntegers',
          'params': {
            'apiKey': RANDOM_TOKEN,
            'min': 1,
            'max': max,
            'n': 1,
          },
          'id': 1,
        }
        encoded_data = dumps(request_data)

        headers = {
          'Content-Type': 'application/json-rpc',  # Тип запроса
        }
        encoded_headers = dumps(headers)

        connection = HTTPSConnection('api.random.org')
        connection.request('GET', '/json-rpc/1/invoke', encoded_data, headers)

        response = connection.getresponse()
        response_data = loads(response.read().decode())

        return response_data['result']['random']['data'][0]

#
def setup(bot):
    bot.add_cog(roll(bot))
