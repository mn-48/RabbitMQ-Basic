import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)


user_payment_message = f"A european user paid for somethings"

channel.basic_publish(exchange='mytopicexchange', routing_key='user.europe.payments', body=user_payment_message)

print(f"sent message: {user_payment_message}")


business_order_message = f"A european business order goods"

channel.basic_publish(exchange='mytopicexchange', routing_key='business.europe.order', body=business_order_message)

print(f"sent message: {business_order_message}")





connection.close()