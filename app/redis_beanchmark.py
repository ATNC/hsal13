import json
import time
from .utils import generate_random_dict_with_random_keys
from redis import Redis


def measure_messages(client: Redis, iterations: int, message: bytes, message_type: str):
    print(f'Measuring {message_type} messages')

    # Push messages into the Redis list
    start = time.time()
    for _ in range(iterations):
        client.lpush("queue", message)
    end = time.time()
    print(f'Time taken to push {iterations} {message_type} messages into Redis:', end - start)

    # Pop messages from the Redis list
    start = time.time()
    for _ in range(iterations):
        client.rpop("queue")
    end = time.time()
    print(f'Time taken to pop {iterations} {message_type} messages from Redis:', end - start)


def measure_small_messages(client: Redis, iterations: int):
    data = json.dumps({'message': 'queue message'}).encode('utf-8')
    print(f'Size of small message: {len(data)} bytes')
    measure_messages(client, iterations, data, 'small')


def measure_large_messages(client: Redis, iterations: int):
    data = json.dumps(generate_random_dict_with_random_keys()).encode('utf-8')
    print(f'Size of large message: {len(data)} bytes')
    measure_messages(client, iterations, data, 'large')


def run(client: Redis, iterations: int = 500_000):
    measure_small_messages(client, iterations)
    measure_large_messages(client, iterations)
    