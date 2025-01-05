import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "B.settings")
django.setup()

# from users.models import User
from django.contrib.auth import get_user_model

params = pika.URLParameters('amqps://tnrngeyk:TfaLRAKQ5U7shQGbkywlnv2dKlNJ2sRL@possum.lmq.cloudamqp.com/tnrngeyk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='B')


def callback(ch, method, properties, body):
    print('Received in B')
    data = json.loads(body)
    # data = body
    # print(data)

    if properties.content_type == 'hello_world':
        # print(body)
        print(data.get("hello", "Empty Str"))

    if properties.content_type == 'new_user_register':
        print("Yes I am Working!!!!!!!!!!")
        print(data)

        User = get_user_model()
        user = User(
            username = data["username"],
            email = data["email"],
            first_name = data["first_name"],
            last_name = data["last_name"],
            date_of_birth = data["date_of_birth"],
            address = data["address"],
        )
        user.save()
        user.set_password(data["password"])
        user.save()

        first_user = User.objects.get(id=1)

        print("user------------------------: ", user)

        print("\n\n\n username", data["username"])


channel.basic_consume(queue='B', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()


# =====================================================
# import pika
# import json
# import os
# import django
# from django.contrib.auth import get_user_model
# from django.db import transaction
# from django.core.exceptions import ValidationError

# # Set up Django environment
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "B.settings")
# django.setup()

# # RabbitMQ connection parameters
# params = pika.URLParameters('amqps://tnrngeyk:TfaLRAKQ5U7shQGbkywlnv2dKlNJ2sRL@possum.lmq.cloudamqp.com/tnrngeyk')

# # Establish connection and channel
# connection = pika.BlockingConnection(params)
# channel = connection.channel()

# # Declare queue
# channel.queue_declare(queue='B')

# def callback(ch, method, properties, body):
#     print('Received in B')
#     data = json.loads(body)

#     if properties.content_type == 'hello_world':
#         print(data.get("hello", "Empty Str"))

#     elif properties.content_type == 'new_user_register':
#         print("Yes I am Working!!!!!!!!!!")
#         print(data)

#         User = get_user_model()
#         try:
#             with transaction.atomic():
#                 user = User(
#                     username=data["username"],
#                     email=data["email"],
#                     first_name=data["first_name"],
#                     last_name=data["last_name"],
#                     date_of_birth=data["date_of_birth"],
#                     address=data["address"],
#                 )
#                 user.set_password(data["password"])
                
#                 # Attempt to save the user
#                 user.save()
#                 print("User saved successfully.")
                
#                 # Fetch user to confirm save
#                 first_user = User.objects.get(id=user.id)
#                 print("User after save:", first_user)

#         except ValidationError as e:
#             print(f"Validation Error: {e}")
#         except Exception as e:
#             print(f"An error occurred while saving the user: {e}")
#         else:
#             print("\n\n\n Username:", data["username"])

# # Start consuming messages
# channel.basic_consume(queue='B', on_message_callback=callback, auto_ack=True)

# print('Started Consuming')

# try:
#     channel.start_consuming()
# except KeyboardInterrupt:
#     print("Interrupted")
# finally:
#     channel.close()
#     connection.close()