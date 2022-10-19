import numpy
import discord
import asyncio
import time
import lxml
from bs4 import BeautifulSoup
import requests
from discord.ext import commands
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

url_of_page = 'https://polygonscan.com/address/0x0dc733a0c086a113a88ddab7c4160dc097b6f89a'


def computequoteprice():
  url_requests = requests.get(url_of_page)
  soup_ocreate = BeautifulSoup(url_requests.text, 'lxml')
  quote_price = soup_ocreate.find('div', class_='col-md-8').text[0:9]
  ###rint(balance)
  #numpy.round(computequoteprice, 2)
  return quote_price


@client.event
async def on_ready():
  print(client.user.name)
  print(client.user.id)
  print("online")
  activity = discord.Game(name="0xTheDoctor is coding...")
  while True:

    activity = discord.Game(name=str(computequoteprice() +
                                     " Matic"))  #.replace(" MATIC", "")
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
    for guild in client.guilds:
      await guild.me.edit(nick="Matic | " + str(computequoteprice()))


@client.command(pass_context=True)
async def ping(ctx):
  await ctx.send('Hello')


client.run(
  'MTAzMTI0NzMzNzAzMDQxODU2NA.GLC2hn.oxEC7ixUr9Ia54Lqa7tdNK25oKPFpEZlOx5vRo')
