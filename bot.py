import discord
import asyncio
import json
from data_collect import *

with open('config.json') as file:
    config = json.load(file)

class DiscordBot():
    pass



# fetchs close prices, calculates rsi and returns rsi if it's over 70 or below 30. otherwise returns False
async def rsi_check():
    prices = fetch_close_prices('SOLUSDT', 60, 100)
    rsi = calculate_rsi(prices)

    if rsi > 70:
        return ['above', rsi]
    elif rsi < 30:
        return ['below', rsi]
    
    return 0
