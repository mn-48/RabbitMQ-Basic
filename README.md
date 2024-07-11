


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

```dotnet run```


# add package

```
dotnet add package RabbitMQ.Client

```






[Link](https://www.youtube.com/watch?v=jXBd0jP6EoE&list=PLalrWAGybpB-UHbRDhFsBgXJM1g6T4IvO&index=9)
