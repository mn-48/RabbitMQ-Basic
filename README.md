


# ---------------- Python ----------------
# Run 

First run `consumer.py`
`python consumer.py`


Then run `producer.py`
`python producer.py`

# install rabbitmq-server 
```
sudo apt-get install -y rabbitmq-server
```

service --status-all

sudo service rabbitmq-server start

sudo service rabbitmq-server status
sudo systemctl status rabbitmq-server


# rabbitmq GUI
```
sudo rabbitmq-plugins enable rabbitmq_management
```

# rabbitmq browser 
```
localhost:15672
```

`username: guest`
`password: guest`

`username: mn48`
`password: testpass1234`



# ---------------- C# ----------------
# create project 
```
makedir producer

cd producer

dotnet new console

```

# run project

```

dotnet run

```


# add package

```
dotnet add package RabbitMQ.Client

```






[Link](https://www.youtube.com/watch?v=jXBd0jP6EoE&list=PLalrWAGybpB-UHbRDhFsBgXJM1g6T4IvO&index=9)


# producer.py

```
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

```

# consumer.py
```
import pika


def on_message_received(ch, method, properties, body):
    print(f"received message: {body}")


connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')


channel.basic_consume(queue="letterbox", auto_ack=True,
                      on_message_callback=on_message_received)


print("starting consuming")


channel.start_consuming()

```