import json

import time
from confluent_kafka import Producer


def print_result(x, y):
    print(x)
    print(y.topic(), y.value())

p = Producer({'bootstrap.servers': 'localhost:9092'})
for data in range(5):
    time.sleep(1)
    p.produce('my-replicated-topic', value=json.dumps(data).encode('utf-8'), on_delivery=print_result)

p.poll(50)
print('I think I should be here')