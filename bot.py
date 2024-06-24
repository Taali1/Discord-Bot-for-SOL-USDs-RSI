import discord
from discord.ext import tasks
from data_collect import *
from dotenv import load_dotenv
import asyncio
import os
from delay import get_delay
import logging
from datetime import datetime

# Loading enviroumental variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Creating log file
logger = logging.getLogger(__name__)
logging.basicConfig(filename='discord_bot.log', level=logging.INFO)

@tasks.loop(seconds=3600)
async def rsi() -> None:
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        print('Checking RSI...')
        logging.INFO(f'{datetime.datetime.now().isoformat(sep=" ", timespec="seconds")} - Checking RSI...')

        rsi_value = await rsi_check()

        logging.INFO(f'{datetime.datetime.now().isoformat(sep=" ", timespec="seconds")} - RSI value is {rsi_value}')

        if rsi_value > 70 or rsi_value < 30:
            print(f'RSI fits and its value is {rsi_value}')
            await channel.send(f'RSI for SOL/USDT is {rsi_value}!\n')
            logging.INFO(f'{datetime.datetime.now().isoformat(sep=" ", timespec="seconds")} - RSI fits and Discord Bot is sending message')
        else:
            print('RSI doesn\'t fit')
            logging.INFO(f'{datetime.datetime.now().isoformat(sep=" ", timespec="seconds")} - RSI doesn\'t fit')
            
    else:
        print('Channel not found')
        logging.INFO(f'{datetime.datetime.now().isoformat(sep=" ", timespec="seconds")} - Channel not found')

@client.event
async def on_ready() -> None:
    channel = client.get_channel(CHANNEL_ID)

    if channel:
        print(f'Bot {client.user} is active now')
        logging.INFO(f'{datetime.datetime.now().isoformat(sep=" ", timespec="seconds")} - Bot {client.user} is active now')
    else:
        logging.INFO(f'{datetime.datetime.now().isoformat(sep=" ", timespec="seconds")} - Channel not found')
        print('Channel not found')

    # Delays bot so he checks RSI only after candel closes/opens
    delay = await get_delay()
    print(f'Bot delayed for {delay} seconds, ergo {delay/60} minutes')
    logging.INFO(f'{datetime.datetime.now().isoformat(sep=" ", timespec="seconds")} - Bot delayed for {delay} seconds, ergo {delay/60} minutes')
    if channel:
        await channel.send(f'Bot delayed for {delay} seconds, ergo {int(delay/60)} minutes and {delay % 60} seconds')
    await asyncio.sleep(delay)
    logging.INFO(f'{datetime.datetime.now().isoformat(sep=" ", timespec="seconds")} - Bot has stopped waiting')
    rsi.start()

if __name__ == '__main__':
    # Initiating Discord bot
    client.run(DISCORD_TOKEN)
    logging.INFO(f'{datetime.now().isoformat(sep=" ", timespec="seconds")} - Running a Discord bot client')