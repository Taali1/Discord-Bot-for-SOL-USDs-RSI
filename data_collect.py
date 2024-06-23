import requests
import json
import pandas as pd

with open('config.json') as file:
    config = json.load(file)

# fetchs candlestick chart from BYBIT API and returns its close prices
def fetch_close_prices(symbol: str = 'SOLUSDT', interval: int = 60, limit: int = 100):
    # sets interval to 1h and returns 100 records
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    columns = ['Start time (ms)', 'Open', 'High', 'Low', 'Close', 'Volume', 'Turnover']
    response = requests.get(config['BYBIT_API_URL'], params=params)

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
    return rsi

data = fetch_close_prices()
print(data)
print(calculate_rsi(data))