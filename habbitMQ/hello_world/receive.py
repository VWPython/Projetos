"""
This will receive messages from the queue and print them on the screen.

RabbitMQ is a message broker: it accepts and forwards messages. You can think
about it as a post office: when you put the mail that you want posting in a post
box, you can be sure that Mr. Postman will eventually deliver the mail to your
recipient.In this analogy, RabbitMQ is a post box, a post office and a postman.

A producer is a user application that sends messages.
A queue is a buffer that stores messages.
A consumer is a user application that receives messages.
"""

import pika  # Python client recommended by the RabbitMQ


def establish_connection(ip_address):
    """
    Establish a connection with RabbitMQ server.

    Return: The connection with RabbitMQ server.
    """

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=ip_address)
    )
    return connection


def create_channel(connection):
    """
    Creates the communication channel with the RabbitMQ server.

    @Param connection: Parameter that will store the connection.

    Return: The channel connection.
    """

    channel = connection.channel()
    return channel


def create_queue(channel, queue):
    """
    Before receive we need to make sure the recipient queue exists.
    Create a hello queue to get message.

    Parameters:

        - channel: The channel conection with the RabbitMQ server.
        - queue: Queue specifies where the message will be delivered.

    Return: Nothing.
    """

    channel.queue_declare(queue=queue)


def callback(ch, method, properties, body):
    """
    It works by subscribing a callback function to a queue.
    Whenever we receive a message, this callback function is called by the Pika
    library. In our case this function will print on the screen the contents of
    the message.

    Return: Nothing.
    """

    print(" [x] Received %r" % body)


def callback_consume(channel, queue):
    """
    We need to tell RabbitMQ that this particular callback function should
    receive messages from our queue.

    Parameters:

        - channel: The channel conection with the RabbitMQ server.
        - queue: Queue specifies where the message will be consumed.

    Return: Nothing.
    """

    channel.basic_consume(callback,
                          queue=queue,
                          no_ack=True)


def wait_for_data(channel):
    """
    We enter a never-ending loop that waits for data and runs callbacks whenever
    necessary.

    Return: Nothing.
    """

    channel.start_consuming()


def main():
    """
    Receive messages from the queue and print them on the screen.
    """

    connection = establish_connection('localhost')
    channel = create_channel(connection)
    create_queue(channel, 'hello')
    callback_consume(channel, 'hello')

    print(' [*] Waiting for messages. To exit press CTRL+C')

    wait_for_data(channel)

if __name__ == '__main__':
    main()
