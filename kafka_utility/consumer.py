import time
from kafka import KafkaConsumer, TopicPartition
from kafka.consumer.fetcher import ConsumerRecord


# auto_offset_reset: A policy for resetting offsets on OffsetOutOfRange errors: ‘earliest’ will move to the oldest available message, ‘latest’ will move to the most recent. Any other value will raise the exception. Default: ‘latest’.
# enable_auto_commit: If True , the consumer’s offset will be periodically committed in the background. Default: True.
consumer = KafkaConsumer(group_id='test-group', auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'], enable_auto_commit=False)

# Assign TopicPartition to consumer
consumer.assign([TopicPartition('my-replicated-topic', 0)])

# Print the next-fetch offset in certain TopicPartition + 1
print(consumer.committed(TopicPartition('my-replicated-topic', 0)))

# Print all partitions of certain topic
print(consumer.partitions_for_topic('my-replicated-topic'))

# Print the offset of the next record that will be fetched
print(consumer.position(TopicPartition('my-replicated-topic', 0)))

# Seek to the oldest available offset for partitions
consumer.seek_to_beginning()
# print(consumer.position(TopicPartition('my-replicated-topic', 0)))

for msg in consumer:
    print(msg)