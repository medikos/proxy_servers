import pytest
from ProxyO.parser import ProxyServer
import faker


@pytest.fixture(scope='function')
def proxy_parser():
    def _proxy_parser(type_=False, data=False):
        if type_:
            fake = faker.Faker()
            fake_dict = dict(
                ip=fake.ipv4(),
                country=fake.country(),
                anonymity=fake.word(),
                uptime=float(fake.random_number())
            )
            return ProxyServer(**fake_dict)
        if data:
            fake_dict = dict(
                ip='127.0.0.1',
                country='FR',
                anonymity='Hello',
                uptime=1.123
            )
            return ProxyServer(**fake_dict)
    return _proxy_parser


def test_type_proxy_server_parser(proxy_parser):
    proxy_server = proxy_parser(type_=True)
    assert type(proxy_server.ip) == str
    assert type(proxy_server.country) == str
    assert type(proxy_server.uptime) == float
    assert type(proxy_server.anonymity) == str


def test_data_proxy_server_parser(proxy_parser):
    proxy_server = proxy_parser(data=True, type_=False)
    assert proxy_server.ip == '127.0.0.1'
    assert proxy_server.country == 'FR'
    assert proxy_server.uptime == 1.123
    assert proxy_server.anonymity == 'Hello'
