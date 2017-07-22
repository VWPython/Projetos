"""
O arquivo txt possui multiplas linhas contendo números
Escreva um objeto thread que consiga acessar uma linha
especifíca do arquivo e le-lo até certo ponto de forma
a obter a soma dos números contidos dentro do arquivo
de maneira mais rápida
"""

import threading

class Le(threading.Thread):
    cont = 0
    stop = 0
    def __init__(self, n, arq, mutex):
        self.n = n
        self.arq = arq
        self.mutex = mutex
        threading.Thread.__init__(self)
    
    def run(self):
        for i in range(0, self.n, 5):
            with self.mutex:
                Le.cont += sum([int(l.rstrip()) for l in self.arq.readlines(10)])

def roda():
    Le.cont = 0
    n = 100000

    with open('num.txt') as arq:
        stdoutmutex = threading.Lock()
        threads = []
    
        for i in range(n):
            thread = Le(int(1000000/n), arq, stdoutmutex)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    print(Le.cont)

if __name__ == '__main__':
    roda()
