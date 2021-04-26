import aiohttp
import asyncio
import pydantic
from typing import Dict, List


class ProxyServer(pydantic.BaseModel):
    country: Dict[str, str]
    ip: str
    anonymity: str
    uptime: float
    port: int


async def request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


class ProxyO:

    def list_proxy(self, country=None, port=None) -> List[ProxyServer]:
        list_proxy = ProxyCreator().create_list_proxy()
        list_proxy = [ProxyServer(**proxy) for proxy in list_proxy]
        if type(country) == str:
            country = country.upper()
            list_proxy = list(filter(lambda x: x.country['iso3166a2'] == country, list_proxy))
        if type(port) == int or type(port) == str:
            port = int(port)
            list_proxy = list(filter(lambda x: x.port == port, list_proxy))
        return list_proxy


class ProxyCreator:
    def create_list_proxy(self):
        res = asyncio.run(request('http://api.foxtools.ru/v2/Proxy/'))['response']['items']
        return res


if __name__ == '__main__':
    proxy_createor = ProxyO()
    list_proxy = proxy_createor.list_proxy()
    print(list_proxy)
    list_proxy = proxy_createor.list_proxy(country='RU')
    print(list_proxy)
    list_proxy = proxy_createor.list_proxy(port=80)
    print(list_proxy)
