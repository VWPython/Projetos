from cliente import Client


def main():
    # Configurações de conexão do servidor
    # O nome do servidor pode ser o endereço de IP ou domínio (www.algo.com)
    server_host = 'localhost'
    server_port = 5000

    for i in range(50):
        operation = '2 + %d' % i
        Client(server_host, server_port, operation).start()


if __name__ == '__main__':
    main()
