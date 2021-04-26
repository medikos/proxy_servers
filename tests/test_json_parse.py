import pytest
from ProxyO.parser import ProxyServer, ProxyO
import faker


@pytest.fixture(scope='function')
def proxy_parser():
    def _proxy_parser(type_=False, data=False):
        if type_:
            fake = faker.Faker()
            fake_dict = dict(
                ip=fake.ipv4(),
                country=dict(),
                anonymity=fake.word(),
                uptime=float(fake.random_number()),
                port=fake.random_number(),
            )
            return ProxyServer(**fake_dict)
        if data:
            fake_dict = dict(
                ip='127.0.0.1',
                country=dict(hello=1),
                anonymity='Hello',
                uptime=1.123,
                port=8080,
            )
            return ProxyServer(**fake_dict)

    return _proxy_parser


def test_type_proxy_server_parser(proxy_parser):
    proxy_server = proxy_parser(type_=True)
    assert type(proxy_server.ip) == str
    assert type(proxy_server.country) == dict
    assert type(proxy_server.uptime) == float
    assert type(proxy_server.anonymity) == str
    assert type(proxy_server.port) == int


def test_data_proxy_server_parser(proxy_parser):
    proxy_server = proxy_parser(data=True, type_=False)
    assert proxy_server.ip == '127.0.0.1'
    assert proxy_server.country == dict(hello='1')
    assert proxy_server.uptime == 1.123
    assert proxy_server.anonymity == 'Hello'
    assert proxy_server.port == 8080


def test_proxy_object():
    proxy_createor = ProxyO()
    assert type(proxy_createor.list_proxy()) == list
    assert type(proxy_createor.list_proxy(country='RU')) == list
    assert type(proxy_createor.list_proxy(port=80)) == list
