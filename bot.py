import discord
from discord.ext import tasks
from data_collect import *
from dotenv import load_dotenv
import asyncio
import os
from delay import get_delay
import logging
from datetime import datetime

# Loading environmental variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Creating log file. You can get access to it in container => main => discord_bot.log
logger = logging.getLogger(__name__)
logging.basicConfig(filename='discord_bot.log', level=logging.INFO)

# function to shorten code
def log(log_message: str) -> None:
    logging.info(f'{datetime.now().isoformat(sep=" ", timespec="seconds")} - {log_message}')

# Cheking of RSI meets conditions. If True prints message to the chat
@tasks.loop(seconds=3600)
async def rsi() -> None:
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        log('Checking RSI...')

        rsi_value = await rsi_check()

        log(f'RSI value is {rsi_value}')

        if rsi_value > 70 or rsi_value < 30:
            await channel.send(f'RSI for SOL/USDT is {rsi_value}!')
            log('RSI fits and Discord Bot is sending message')
        else:
            log(f'RSI doesnt fit. Its value is {rsi_value}')

    else:
        log('Channel not found')

@client.event
async def on_ready() -> None:
    channel = client.get_channel(CHANNEL_ID)

    if channel:
        log(f'Bot {client.user} is active now')
    else:
        log('Channel not found')

    # Delays bot so he checks RSI only after candel closes/opens
    delay = await get_delay()
    if channel:
        log(f'Bot delayed for {delay} seconds, ergo {int(delay/60)} minutes and {delay % 60} second')
    await asyncio.sleep(delay)

    # Starts checking RSI every 1 hour
    log('Bot has stopped waiting')
    if not rsi.is_running():
        rsi.start()

if __name__ == '__main__':
    # Initiating Discord bot
    log('Running a Discord bot client')
    client.run(DISCORD_TOKEN)
    