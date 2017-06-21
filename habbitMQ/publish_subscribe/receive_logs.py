"""
Simple logging system that receive and print log menssages.

In our logging system every running copy of the receiver program will get the
messages. That way we'll be able to run one receiver and direct the logs to
disk; and at the same time we'll be able to run another receiver and see the
logs on the screen

Essentially, published log messages are going to be broadcast to all the
receivers.

We'll deliver a message to multiple consumers.
This pattern is known as "publish/subscribe".
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

    Parameters:

        - connection: Parameter that will store the connection.

    Return: The channel connection.
    """

    channel = connection.channel()
    return channel


def fanout_exchange_type_declare(channel, exchange_name):
    """
    Declare an exchange of type fanout that send messages to an exchange and
    the exchange must know exactly what to do with a message it receives

    On one side it receives messages from producers and the other side it pushes
    them to queues.

    The rules for that are defined by the exchange type (fanout) it just
    broadcasts all the messages it receives to all the queues it knows.

    Parameters:

        - channel: The channel connection.
        - exchange_name: Name of the exchange of type fanout

    Return: Nothing
    """

    channel.exchange_declare(exchange=exchange_name, type='fanout')


def create_temporary_queue(channel):
    """
    Hear about all log messages, not just a subset of them, and it is also
    interested only in currently flowing messages not in the old ones.

    Connect to Rabbit we need a fresh, empty queue. To do it we could create a
    queue with a random name

    Once we disconnect the consumer the queue should be deleted.

    Parameters:

        - channel: The channel connection

    Return: The random queue name
    """

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    return queue_name


def binding(channel, exchange_name, queue_name):
    """
    Tell the exchange to send messages to our queue. That relationship between
    exchange and a queue is called a binding.
    """

    channel.queue_bind(exchange=exchange_name, queue=queue_name)


def callback(ch, method, properties, body):
    """
    It works by subscribing a callback function to a queue.
    Whenever we receive a message, this callback function is called by the Pika
    library. In our case this function will print on the screen the contents of
    the message.

    Return: Nothing.
    """

    print(" [x] Received %r" % body)


def callback_consume(channel, queue_name):
    """
    We need to tell RabbitMQ that this particular callback function should
    receive messages from our queue.

    Parameters:

        - channel: The channel conection with the RabbitMQ server.
        - queue: Queue specifies where the message will be consumed.

    Return: Nothing.
    """

    channel.basic_consume(callback,
                          queue=queue_name,
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
    Simple logging system that receive and print log messages.
    """

    connection = establish_connection('localhost')
    channel = create_channel(connection)
    fanout_exchange_type_declare(channel, 'logs')
    queue_name = create_temporary_queue(channel)
    binding(channel, 'logs', queue_name)
    callback_consume(channel, queue_name)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    wait_for_data(channel)

if __name__ == '__main__':
    main()
