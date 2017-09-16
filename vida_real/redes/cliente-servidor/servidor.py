# Importa os modulos
from socketserver import BaseRequestHandler, ThreadingTCPServer
from ast import literal_eval
import time

OPERATOR = 0
VALUE1 = 1
VALUE2 = 2


def configure_server():
    """
    Configura o servidor com o host e a porta
    """

    server_host = ''
    server_port = 5000
    return (server_host, server_port)


def now():
    """
    Devolve a hora atual
    """

    return time.ctime(time.time())


def get_list(data):
    """
    Transforma a string recebida em uma lista
    """

    try:
        data = literal_eval(data.decode())
    except (SyntaxError, ValueError):
        pass

    return data


class HandlesClientRequests(BaseRequestHandler):
    """
    Classe que lida com as requisições do cliente.
    """

    def handle(self):
        # Lida com cada requisição do cliente
        print(self.client_address, now())

        while True:
            # Recebe dados enviados pelo cliente e decodifica eles
            data = self.request.recv(1024)

            data = get_list(data)

            # Se não receber nada paramos o loop
            if not data:
                break

            if data[OPERATOR] == 'add':
                result = '{data}'.format(
                    data=self.add(data[VALUE1], data[VALUE2])
                )
            elif data[OPERATOR] == 'sub':
                result = '{data}'.format(
                    data=self.subtract(data[VALUE1], data[VALUE2])
                )
            elif data[OPERATOR] == 'div':
                result = '{data}'.format(
                    data=self.divide(data[VALUE1], data[VALUE2])
                )
            else:
                result = '{data}'.format(
                    data=self.multiply(data[VALUE1], data[VALUE2])
                )

            # Servidor manda de volta a resposta
            self.request.send(result.encode())

        # Fecha a conexão criada depois de responder o cliente
        self.request.close()

    def add(self, value1, value2):
        """
        Soma os dois valores inteiros.
        """

        return [0, int(value1) + int(value2)]

    def subtract(self, value1, value2):
        """
        Subtrai dois valores inteiros
        """

        return [0, int(value1) - int(value2)]

    def multiply(self, value1, value2):
        """
        Multiplica dois valores inteiros
        """

        return [0, int(value1) * int(value2)]

    def divide(self, value1, value2):
        """
        Divide dois valores inteiros
        """

        if int(value2) == 0:
            return [1, 'Não pode haver divisão por zero']
        else:
            return [0, int(value1) / int(value2)]


def main():
    ip_address = configure_server()
    server = ThreadingTCPServer(ip_address, HandlesClientRequests)
    server.serve_forever()


if __name__ == '__main__':
    main()
