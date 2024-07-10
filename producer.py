import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

message = "This is my first message"
# message = input()


channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"Sent message: {message}")

connection.close()
