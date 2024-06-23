import discord
from discord.ext import tasks
import asyncio
import json
from data_collect import *

with open('config.json') as file:
    config = json.load(file)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@tasks.loop(seconds=3600)
async def rsi():
    channel = client.get_channel(1254198350454984749)
    if channel:
        print('Checking rsi...')
        rsi_value = rsi_check()

        if rsi_value:
            print(f'RSI fits and its value is {rsi_value}')
            channel.send(f'RSI for SOL/USDT is {rsi_value}!')
        else:
            print('RSI doesn\'t fit')
    else:
        print('Channel not found')

@client.event
async def on_ready():
    channel = client.get_channel(1254198350454984749)
    print(f'Logged in as {client.user}')
    if channel:
        await channel.send(f'Bot {client.user} is active now')
        rsi.start()
    else:
        print('Channel not found')


if __name__ == '__main__':
    client.run(config["DISCORD-TOKEN"])