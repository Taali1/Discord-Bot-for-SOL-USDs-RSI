import pandas as pd
from dotenv import load_dotenv
import os
import asyncio
import aiohttp

# Loading environmental variables
load_dotenv()
BYBIT_API_KEY  = os.getenv('BYBIT_API_KEY')
BYBIT_API_URL = os.getenv('BYBIT_API_URL')

# fetchs candlestick chart from BYBIT API and returns its close prices
async def fetch_close_prices(symbol: str = 'SOLUSDT', interval: int = 60, limit: int = 100):
    # sets interval to 1h and returns 100 records for more reliable results
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }

    # Column headers that that are returned in response. Added for readablility
    columns = ['Start time (ms)', 'Open', 'High', 'Low', 'Close', 'Volume', 'Turnover']

    # Geting data from BYBIT API and selects only Close prices
    async with aiohttp.ClientSession() as session:
        async with session.get(BYBIT_API_URL, params=params) as response:
            data = await response.json()
            df = pd.DataFrame(data['result']['list'], columns = columns)
            prices = df.Close.astype(float)

    return prices

# This took me some time to write and understand. I knew what RSI is but never calculated it.
async def calculate_rsi(prices, period: int = 14) -> float:
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = ((delta.where(delta < 0, 0))*-1).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]

# launching two fuctions for rsi calculation for readability
async def rsi_check() -> float:
    prices = await fetch_close_prices('SOLUSDT', 60, 100)
    rsi = await calculate_rsi(prices)

    return rsi