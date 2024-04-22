import redis
from .redis_beanchmark import run


if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6380, db=0)
    r.flushall()
    run(r)

