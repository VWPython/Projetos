from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from ast import literal_eval
from time import sleep

VALUE_1 = 0
OPERATOR = 1
VALUE_2 = 2
STATUS = 0
RESULT = 1


class Client(Thread):
    """
    Classe que realiza gera as operações - Cliente.
    """

    def __init__(self, server, port, operation):
        # Servidor a ser conectado
        self.server = server

        # Porta a ser usada
        self.port = port

        # Operação a ser realizado
        self.operation = operation

        Thread.__init__(self)

    def run(self):
        # Criamos o socket e o conectamos ao servidor
        connection = socket(AF_INET, SOCK_STREAM)
        connection.connect((self.server, self.port))

        # Enviar o pacote para o servidor
        operation = self.operation.split()[OPERATOR]
        if "+" in operation:
            self.send('add', connection)
        elif "-" in operation:
            self.send('sub', connection)
        elif "/" in operation:
            self.send('div', connection)
        elif "x" in operation:
            self.send('mul', connection)
        else:
            print("Operação invalida: Insira como operador +, -, / ou x")

        # Depois de mandar o pacote esperamos a resposta do servidor
        data = connection.recv(1024).decode()

        result = self.get_list(data)

        self.print_result(result)

        connection.close()

    def send(self, operator, connection):
        """
        Envia o pacote para o servidor
        O pacote apresenta a operação o primeiro valor e o segundo valor
        """

        package = [
            operator,
            self.operation.split()[VALUE_1],
            self.operation.split()[VALUE_2]
        ]
        connection.send(str(package).encode())

    def get_list(self, data):
        """
        Transforma a string recebida em uma lista
        A lista apresenta o resultado e o status do resultado 0 é sucesso e
        1 é falha com sua respectiva string de falha.
        """

        try:
            data = literal_eval(data)
        except (SyntaxError, ValueError):
            pass

        return data

    def print_result(self, result):
        """
        Imprime o resultado do servidor
        """

        if result[STATUS] == 0:
            print(
                "{operation} = {result}"
                .format(
                    operation=self.operation,
                    result=result[RESULT]
                )
            )
        else:
            print("Erro: {error}".format(error=result[RESULT]))


def main():
    # Configurações de conexão do servidor
    # O nome do servidor pode ser o endereço de IP ou domínio (www.algo.com)
    server_host = 'localhost'
    server_port = 5000

    running = True

    while running:
        print("Calculadora de expressões simples (+, -, / e x)")
        operation = input("Insira a expressão a ser calculada: ")
        Client(server_host, server_port, operation).start()

        # Espera até receber a resposta
        sleep(0.5)

        # Verificamos se o usuário deseja fazer outra operação
        option = input("Deseja realizar outra operação? (S/N): ").upper()
        if option.startswith("S"):
            running = True
        else:
            print("Finalizando o programa...")
            running = False


if __name__ == '__main__':
    main()
