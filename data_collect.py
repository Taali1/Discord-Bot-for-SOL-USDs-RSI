import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
BYBIT_API_KEY  = os.getenv('BYBIT_API_KEY')
BYBIT_API_URL = os.getenv('BYBIT_API_URL')

# fetchs candlestick chart from BYBIT API and returns its close prices
def fetch_close_prices(symbol: str = 'SOLUSDT', interval: int = 60, limit: int = 100):
    # sets interval to 1h and returns 100 records
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    columns = ['Start time (ms)', 'Open', 'High', 'Low', 'Close', 'Volume', 'Turnover']
    response = requests.get(BYBIT_API_URL, params=params)

    df = pd.DataFrame(response.json()['result']['list'], columns = columns)
    data = df.Close.astype(float)

    return data

# This took me some time to understand. I knew what RSI is but never calculated it
def calculate_rsi(prices, period: int = 14) -> float:
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = ((delta.where(delta < 0, 0))*-1).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]

# fetchs close prices, calculates rsi and returns rsi if it's over 70 or below 30. otherwise returns False
def rsi_check() -> float:
    prices = fetch_close_prices('SOLUSDT', 60, 100)
    rsi = calculate_rsi(prices)

    print(f'RSI: {rsi}')

    if rsi > 70 or rsi < 30:
        return rsi
    return None