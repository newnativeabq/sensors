# test_redis_pubsub.py


import pytest
import redis


@pytest.fixture
def rcon():
    return redis.Redis(host='localhost', port=6379, db=0)


def test_redis_sub(rcon):
    assert rcon.get('nonsense') is None


def test_redis_pub(rcon):
    rcon.set('foo', 'bar')
    assert rcon.get('foo') == b'bar'