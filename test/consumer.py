from confluent_kafka import Consumer, KafkaError

# Configure the Kafka consumer
consumer_config = {
    'bootstrap.servers': '3.135.202.131:30094',  # Replace with your Kafka broker(s) address
    'client.id': 'python-producer',
    'auto.offset.reset': 'earliest',
    'group.id': 'my-group',
}

consumer = Consumer(consumer_config)

# Subscribe to a Kafka topic
topic = 'postgres-demo'
consumer.subscribe([topic])

# Consume messages from the topic
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print(f'Reached end of partition: {msg.topic()} [{msg.partition()}]')
        else:
            print(f'Error while consuming message: {msg.error()}')
    else:
        print(f'Received message: {msg.value().decode("utf-8")}')

# Close the consumer when done
consumer.close()
