import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "B.settings")
django.setup()

params = pika.URLParameters('amqps://tnrngeyk:TfaLRAKQ5U7shQGbkywlnv2dKlNJ2sRL@possum.lmq.cloudamqp.com/tnrngeyk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='B')


def callback(ch, method, properties, body):
    print('Received in B')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'hello_world':
        # print(body)
        print(data.get("hello", "Empty Str"))

channel.basic_consume(queue='B', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()