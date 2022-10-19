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

    msg = '{0.author.mention} function not available contact @0xTheDoctor ;)'.format(
      message)
    await message.channel.send(msg)


#async def bscapi():


@client.event
async def on_ready():
  print(client.user.name)
  print(client.user.id)
  print("online")
  YOUR_API_KEY = "6EVAPAQT7CD2N7H8QPZBCIW1SFXEK6WAP6"

  activity = discord.Game(name="0xTheDoctor is coding...")
  while True:
    async with BscScan(YOUR_API_KEY) as bsc:
      num = await bsc.get_acc_balance_by_token_contract_address(
        contract_address="0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
        address="0xfBbc24CA5518898fAe0d8455Cb265FaAA66157C9")
      num1= int(num[:-18])
      numcomma=format (num1, ',d')  

    activity = discord.Game(name=numcomma + " BUSD")
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
    for guild in client.guilds:
      await guild.me.edit(nick="BUSD | " + numcomma)


@client.command(pass_context=True)
async def ping(ctx):
  await ctx.send('Hello')


client.run(
  'MTAzMTU1MzU0NDk5NTczNzY2MA.GWKyHB.-gS8AcGkQLmUB0bIG0Or2CZ3_xGpjH6uGL38sM')
