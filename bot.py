import discord
from discord.ext import tasks
from data_collect import *
from dotenv import load_dotenv
import os
from bybit_server_time import *


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@tasks.loop(seconds=10)
async def rsi():
    channel = client.get_channel(CHANNEL_ID)
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
    channel = client.get_channel(CHANNEL_ID)
    print(f'Logged in as {client.user}')
    if channel:
        print(f'Bot {client.user} is active now')
        rsi.start()
    else:
        print('Channel not found')


if __name__ == '__main__':
    client.run(DISCORD_TOKEN)