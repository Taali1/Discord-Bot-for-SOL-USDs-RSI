import requests
import json
import pandas as pd


with open('config.json') as file:
    config = json.load(file)

def fetch_kline(symbol: str, interval: int, limit: int ):
    # sets interval to 1h and returns 100 records
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }

    response = requests.get(config['BYBIT_API_URL'], params=params)
    
    return response.json()['result']

# This took me some time to understand. I knew what RSI is but never calculated it
def calculate_rsi(prices, period: int = 14) -> float:
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = ((delta.where(delta < 0, 0))*-1).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def 