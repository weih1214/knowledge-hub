import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# How to encode an integer
# producer.send('my-replicated-topic', bytes(str(1), 'ascii'))
# producer.flush()

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)


def on_send_error(excp):
    print('there is something wrong', excp)


# for i in range(100):
#     producer.send('my-replicated-topic', i).add_callback(on_send_success).add_errback(on_send_error).get()
#     print('hahaha')

producer.send('my-replicated-topic', 9999).add_callback(on_send_success)
producer.flush()
