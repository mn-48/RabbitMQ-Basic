import pika, json, os, django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
# django.setup()

params = pika.URLParameters('amqps://tnrngeyk:TfaLRAKQ5U7shQGbkywlnv2dKlNJ2sRL@possum.lmq.cloudamqp.com/tnrngeyk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='A')


def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'hello_world':
        # print(body)
        print(data.get("hello", "Empty Str"))
    


channel.basic_consume(queue='A', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()