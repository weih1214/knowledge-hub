import json

from kafka import KafkaConsumer, TopicPartition

# auto_offset_reset: A policy for resetting offsets on OffsetOutOfRange errors: ‘earliest’ will move to the oldest available message, ‘latest’ will move to the most recent. Any other value will raise the exception. Default: ‘latest’.
# enable_auto_commit: If True , the consumer’s offset will be periodically committed in the background. Default: True.

consumer = KafkaConsumer('my-replecated-topic', group_id='test-group', auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'], enable_auto_commit=False, value_deserializer=lambda m:json.loads(m.decode('utf-8')))

# Assign TopicPartition to consumer
# consumer.assign([TopicPartition('my-replicated-topic', 0)])

# Print the next-fetch offset in certain TopicPartition + 1
print(consumer.committed(TopicPartition('my-replicated-topic', 0)))

# Print all partitions of certain topic
print(consumer.partitions_for_topic('my-replicated-topic'))

# Print the offset of the next record that will be fetched
print(consumer.position(TopicPartition('my-replicated-topic', 0)))

# Seek to the oldest available offset for partitions
# consumer.seek_to_beginning()
consumer.seek_to_end()

# print(consumer.position(TopicPartition('my-replicated-topic', 0)))


# Consumption method 1
for msg in consumer:
    print(msg)

# Consumption method 2
while True:
    raw_messages = consumer.poll(timeout_ms=1000, max_records=100)
    for topic_partition, messages in raw_messages.items():
        for message in messages:
            application_message = message.value
