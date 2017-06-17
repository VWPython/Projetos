"""
Simple logging system that emit log messages

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
import sys  # Provides access to some variables used by the interpreter


def establish_connection():
    """
    Establish a connection with RabbitMQ server.

    Return: The connection with RabbitMQ server.
    """

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
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


def create_message():
    """
    Create a message that will be send to log system.

    Return: Message
    """

    message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    return message


def publish_exchange_name(channel, exchange_name, message):
    """
    Creates an exchange without a defined queue and insert a message on it and
    print the message

    Parameters:

        - channel: The channel connection
        - exchange_name: Name of exchange
        - message: Message that will be published

    Return: Nothing
    """

    channel.basic_publish(exchange=exchange_name,
                          routing_key='',
                          body=message)

    print(" [x] Sent %r" % message)


def close_connection(connection):
    """
    Before exiting the program we need to make sure the network buffers were
    flushed and our message was actually delivered to RabbitMQ. We can do it
    by gently closing the connection

    Parameters:

        - connection: Parameter that will store the connection

    Return: Nothing
    """

    connection.close()


def main():
    """
    Simple logging system that emit log messages
    """

    connection = establish_connection()
    channel = create_channel(connection)
    fanout_exchange_type_declare(channel, 'logs')
    message = create_message()
    publish_exchange_name(channel, 'logs', message)
    close_connection(connection)

if __name__ == '__main__':
    main()
