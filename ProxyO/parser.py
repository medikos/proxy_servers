import aiohttp
import asyncio
import pydantic


class ProxyServer(pydantic.BaseModel):
    country: str
    ip: str
    anonymity: str
    uptime: float


async def request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


if __name__ == '__main__':
    s = asyncio.run(request('http://api.foxtools.ru/v2/Proxy/'))
