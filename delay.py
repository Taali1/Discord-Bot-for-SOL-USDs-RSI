import requests

# Gets time to  know when to check RSI
def get_time() -> int:
    # Fetch data about server time on BYBIT
    response = requests.get('https://api.bybit.com/v5/market/time').json()
    
    # Get time from response
    time = response['result']['timeSecond']

    return int(time)

def get_delay(server_time: int) -> int:
    # 3 600 000 is 1 hour in milliseconds
    delay = server_time % 3600000

    return delay
