import discord 
from discord.ext import commands
from collections import namedtuple
import requests
from lxml import html

client = commands.Bot(command_prefix="/")

covid_data = namedtuple("covid_data", "cases deaths recovered")


def covid_stats(url: str = "https://www.worldometers.info/coronavirus/") -> covid_data:
    xpath_str = '//div[@class = "maincounter-number"]/span/text()'
    return covid_data(*html.fromstring(requests.get(url).content).xpath(xpath_str))


fmt = """:worm: **Total COVID-19 cases in the world:** `{}`

:skull: **Total deaths due to COVID-19 in the world:** `{}`

:health_worker: **Total COVID-19 patients recovered in the world:** `{}`"""

@client.event
async def on_ready():
	print ("Bot is ready")

@client.command()
async def covid(ctx):
	await ctx.send(fmt.format(*covid_stats()))

client.run('#Your Bot token here')
