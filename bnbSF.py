import numpy
import discord
import asyncio
import time
import lxml
from bscscan import BscScan
from bs4 import BeautifulSoup
import requests
from discord.ext import commands
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
YOUR_API_KEY = "6EVAPAQT7CD2N7H8QPZBCIW1SFXEK6WAP6"

url_of_page = 'https://polygonscan.com/address/0x0dc733a0c086a113a88ddab7c4160dc097b6f89a'

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):

      msg = '{0.author.mention} shut up bitch'.format(message)
      await message.channel.send(msg)

    if message.content.startswith('!checkping'):

      msg = '{0.author.mention} function not available contact @0xTheDoctor ;)'.format(message)
      await message.channel.send(msg)





#async def bscapi():

 

@client.event
async def on_ready():
  print(client.user.name)
  print(client.user.id)
  print("online")
  
  activity = discord.Game(name="0xTheDoctor is coding...")
  while True:
    async with BscScan(YOUR_API_KEY) as bsc:
      num = await bsc.get_bnb_balance(address="0x4F2bC1d99C953e0053F5bb9A6855CF7A5CBe66Fa")
      num1= int(num[:-18])
      numcomma=format (num1, ',d')
  
    activity = discord.Game(name= numcomma +" BNB")
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
    for guild in client.guilds:
      await guild.me.edit(nick="BNB | " + numcomma)




@client.command(pass_context=True)
async def ping(ctx):
  await ctx.send('Hello')


client.run('MTAzMTU3MDg1NjUwMzE0ODYzNA.Gmi3OO.j0MS-7cX4DZXkssLzpL1teqROQAHXAk-zeJPV8')
