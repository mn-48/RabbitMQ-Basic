using System.Text;
using RabbitMQ.Client;

var factory = new ConnectionFactory { HostName = "localhost" };
using var connection = factory.CreateConnection();
using var channel = connection.CreateModel();

channel.QueueDeclare(queue: "letterbox",
                     durable: false,
                     exclusive: false,
                     autoDelete: false,
                     arguments: null);

const string message = "This is my first message";
var body = Encoding.UTF8.GetBytes(message);

channel.BasicPublish(exchange: string.Empty,
                     routingKey: "letterbox",
                     basicProperties: null,
                     body: body);


Console.WriteLine($" Publish Message: {message}");

// Console.WriteLine(" Press [enter] to exit.");
// Console.ReadLine();