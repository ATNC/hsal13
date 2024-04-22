import json
import time
from pystalk import BeanstalkClient as Client
from .utils import generate_random_dict_with_random_keys

client = Client('localhost', 11300)


def measure_messages(iterations: int, message: str, message_type: str):
    print(f'Measuring {message_type} messages')
    start = time.time()
    for i in range(iterations):
        client.put_job(message)
    end = time.time()
    print(f'Time taken to put {iterations} {message_type} messages into Beanstalkd:', end - start)
    start = time.time()
    for job in client.reserve_iter():
        client.delete_job(job)
    end = time.time()
    print(f'Time taken to read {iterations} {message_type} messages from Beanstalkd:', end - start)


def measure_small_messages(iterations: int):
    data = {'message': 'queue message'}
    measure_messages(iterations, json.dumps(data), 'small')


def measure_large_messages(iterations: int):
    data = generate_random_dict_with_random_keys()
    measure_messages(iterations, json.dumps(data), 'large')


if __name__ == '__main__':
    iterations = 500_000

    measure_small_messages(iterations)
    measure_large_messages(iterations)
