import asyncio
import aiohttp

# Gets time to  know when to check RSI
async def get_time() -> int:
    URL = 'https://api.bybit.com/v5/market/time'

    # Fetch data about server time on BYBIT
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            # Get time from response
            data = await response.json()
            time = data['result']['timeSecond']
    return int(time)

async def get_delay() -> int:
    # returns server time in seconds
    server_time = await get_time()

    # 3 600 seconds equals to 1 hour ofc
    delay = 3600 - (server_time % 3600) # 3600 will be enough considering additional delay in calculations

    return delay
