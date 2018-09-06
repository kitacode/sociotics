import aiohttp
from async_timeout import timeout


async def Request(url):
    connect = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(connector=connect) as session:
        return await Response(session, url)


async def Response(session, url):
    with timeout(30):
        async with session.get(url) as response:
            return await response.text()
