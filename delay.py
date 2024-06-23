import requests

# Gets time to  know when to check RSI
def get_time() -> int:
    # Fetch data about server time on BYBIT
    response = requests.get('https://api.bybit.com/v5/market/time').json()
    
    # Get time from response
    time = response['result']['timeSecond']

    return time

def get_delay() -> int:
    # returns server time in seconds
    server_time = get_time()

    # 3 600 seconds equals to 1 hour ofc
    delay = server_time % 3600

    return delay
