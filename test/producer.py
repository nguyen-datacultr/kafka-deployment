from confluent_kafka import Producer

# Define a callback function to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Configure the Kafka producer
producer_config = {
    'bootstrap.servers': '3.135.202.131:30094',  # Replace with your Kafka broker(s) address
    'client.id': 'python-producer'
}

producer = Producer(producer_config)

# Produce a message to a Kafka topic
topic = "postgres-demo"
key = "test-key-1"
value = "Hello world! 01"
producer.produce(topic, key=key, value=value, callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()
