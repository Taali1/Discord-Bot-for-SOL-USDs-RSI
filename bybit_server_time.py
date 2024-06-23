import requests

# Gets time to  know when to check RSI
def get_time():
    # Fetch data about server time on BYBIT
    response = requests.get('https://api.bybit.com/v5/market/time').json()
    
    # Get time from response
    time = response['result']['timeSecond']

    return time

print(get_time())