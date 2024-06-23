import discord
from discord.ext import tasks
from data_collect import *
from dotenv import load_dotenv
import asyncio
import os
from delay import get_delay

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@tasks.loop(seconds=3600)
async def rsi():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        print('Checking rsi...')
        rsi_value = rsi_check()

        if rsi_value is not None:
            print(f'RSI fits and its value is {rsi_value}')
            await channel.send(f'RSI for SOL/USDT is {rsi_value}!\n')
        else:
            print('RSI doesn\'t fit')
            await channel.send(f'RSI for SOL/USDT is and didnt fit {rsi_value}!\n')
    else:
        print('Channel not found')

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)

    print(f'Logged in as {client.user}')

    if channel:
        print(f'Bot {client.user} is active now')
        await channel.send(f'Bot {client.user} is active now')
    else:
        print('Channel not found')

    # Delays bot so he checks RSI only after candel closes/opens
    delay = get_delay()
    print(f'Bot delayed for {delay} seconds, ergo {delay/60} minutes')
    if channel:
        await channel.send(f'Bot delayed for {delay} seconds, ergo {int(delay/60)} minutes and {delay % 60} seconds')
    await asyncio.sleep(delay)

    rsi.start()

if __name__ == '__main__':
    client.run(DISCORD_TOKEN)