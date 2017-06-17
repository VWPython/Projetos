"""
This program will send a single message to the queue.

RabbitMQ is a message broker: it accepts and forwards messages. You can think
about it as a post office: when you put the mail that you want posting in a post
box, you can be sure that Mr. Postman will eventually deliver the mail to your
recipient.In this analogy, RabbitMQ is a post box, a post office and a postman.
"""

import pika  # Python client recommended by the RabbitMQ


def establish_connection():
    """
    Establish a connection with RabbitMQ server

    Return: The connection with RabbitMQ server
    """

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    return connection


def create_channel(connection):
    """
    Creates the communication channel with the RabbitMQ server

    Parameters:

        - connection: Parameter that will store the connection

    Return: The channel connection
    """

    channel = connection.channel()
    return channel


def create_queue(channel, queue):
    """
    Before sending we need to make sure the recipient queue exists.
    Create a hello queue to which the message will be delivered

    Parameters:

        - channel: The channel conection with the RabbitMQ server
        - queue: Especific queue that the message should go.

    Return: Nothing
    """

    channel.queue_declare(queue=queue)


def queue_exchange(channel, queue, message):
    """
    In RabbitMQ a message can never be sent directly to the queue, it always
    needs to go through an exchange. This exchange allows us to specify
    exactly to which queue the message should go.

    Parameters:

        - channel: The channel conection with the RabbitMQ server.
        - queue: Especific queue that the message should go.
        - message: Message that will be sent to the queue

    Return: Nothing.
    """

    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=message)

    print(" [x] Sent 'Hello World!'")


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
    Send a single message to the queue.
    """

    connection = establish_connection()
    channel = create_channel(connection)
    create_queue(channel, 'hello')
    queue_exchange(channel, 'hello', 'Hello World')
    close_connection(connection)

if __name__ == '__main__':
    main()
