import pika
import uuid


def on_replay_message_received(ch, method, properties, body):
    print(f"Replay received message: {body}")


connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

reply_to = channel.queue_declare(queue='', exclusive=True)

channel.basic_consume(queue=reply_to.method.queue, auto_ack=True,
                      on_message_callback=on_replay_message_received)


channel.queue_declare(queue='request-queue')


message = "Can I request a replay?"

cor_id = str(uuid.uuid4())

print(f"Senting Request: {cor_id}")


channel.basic_publish(
    exchange='',
    routing_key='request-queue',
    properties=pika.BasicProperties(
        reply_to=reply_to.method.queue,
        correlation_id=cor_id,
    ),
    body=message)

print(f"Senting Client")

channel.start_consuming()
