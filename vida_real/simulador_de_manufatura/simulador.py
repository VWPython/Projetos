"""
Vamos criar um simulador simples de manufatura
Para isso vamos usar os conceitos de execução.

O sistema funciona da seguinte forma:
1 - Uma fábrica funciona 12h por dia
2 - Há 30 peças a serem produzidas por hora
3 - Há 3 máquinas para produzir as peças
4 - Cada máquina só pode processar uma peça por vez
5 - Cada máquina leva de 2 a 7 minutos para produzir a peça
6 - Cerca de 80% das vezes a peça é feita com sucesso

Simule o sistema funcionando e forneça uma tabela com os seguintes
dados:
1 - Número de peças a serem produzidas geradas
2 - Número de peças processadas com sucesso
3 - Número de peças falhas
4 - Número de peças em espera
5 - Número de peça produzidas em cada máquina
6 - Número de peças falhas em cada máquina
7 - Tempo médio de processamento
8 - Tempo médio de processamento de cada máquina
"""
import time, random, csv, queue, threading

# Fila de peças a serem processadas
fila = queue.Queue()

# Lock para obter dados de forma segura
lock = threading.Lock()

class Gera(threading.Thread):
    """
    Classe que gera cada peça por hora
    """
    def __init__(self, ph, dh, r):
        # Peças geradas por hora
        self.ph = ph
       
        # Número de horas no dia
        self.dh = dh

        # Registradora
        self.r = r

        threading.Thread.__init__(self)

    def run(self):
        # Para cada hora do dia
        for i in range(self.dh):
            # Para cada peça por hora
            for i in range(self.ph):
                # Colocamos uma peça na fila
                fila.put("Peça")

            with lock:
                # E mandamos registras as novas peças
                self.r.registra_novas(self.ph)

            # Nós durmimos por 1 hora= 1 segundo
            time.sleep(1)

class Máquina(threading.Thread):
    """
    Classe que simula a máquina que processa as peças
    """
    def __init__(self, tmin, tmax, f_p, m, registradora):
        # Tempo mínimos de trabalho
        self.tmin = tmin
       
        # Tempo máximo de trabalho
        self.tmax = tmax

        # Porcentagem de chance de fracasso no processo
        self.f_p = f_p
        
        # Número da máquina
        self.m = m

        # Registradora de dados
        self.r = registradora

        threading.Thread.__init__(self)

        # Queremos que a thread feche ao fechar o progrma
        self.daemon = True

    def run(self):
        # Vamos rodar até o programa terminar
        while True:
            try:
                # Tentamos pegar uma peça na fila
                p = fila.get()
            except queue.Empty:
                pass
            else:
                with lock:
                    # Informamos que vamos processar a pessa
                    print("Máquina %i processando peça"%(self.m+1))
                
                # Processamos a peça num tempo t
                t = random.uniform(self.tmin, self.tmax)
                time.sleep(t)
                
                with lock:
                    # Registramos o tempo t de trabalho
                    self.r.registra_tempo(self.m, t)
                    
                    # Depois nós calculamos se a peça deve falhar ou ter sucesso e registramos
                    # esse dado
                    if random.randint(0, 100) > self.f_p:
                        self.r.registra_fracasso(self.m)
                    else:
                        self.r.registra_sucesso(self.m)
        

class Registradora(object):
    """
    Classe que irá juntar todos os dados e coloca-los
    na tabela
    """
    def __init__(self, ms):
        # Sucesso para cada máquina
        self.sucesso = [0 for i in range(ms)]
        
        # Falha para cada máquina
        self.falha = [0 for i in range(ms)]

        # Tempo total de processamento para cada máquina
        self.t = [0 for i in range(ms)]

        # Número total de peças geradas
        self.total = 0

        # Número total de máquinas
        self.ms = ms

    def registra_sucesso(self, m):
        self.sucesso[m] += 1

    def registra_fracasso(self, m):
        self.falha[m] += 1

    def registra_tempo(self, m, t):
        self.t[m] += t

    def registra_novas(self, n):
        self.total += n

    def registra(self):
        # Abrimos o arquivo no modo append
        with open('resultados.csv', 'a') as arq:
            # Criamos o writer do arquivo
            writer = csv.writer(arq)

            # Escrevemos o título dos dados gerais
            writer.writerow(('Peças Geradas', 'Peças com Sucesso', 'Peças falhas', 'Peças em espera', 'Tempo médio de processamento (min)'))

            # Calculamos o número total de sucesso, falha e o tempo médio de processamento
            sucesso = sum(self.sucesso)
            falha = sum(self.falha)
            tempo = 60*sum(self.t)/(sucesso+falha)
            
            # Escrevemos esses dados na tabela
            writer.writerow((self.total, sucesso, falha, fila.qsize(), tempo))

            # Pulamos uma linha
            writer.writerow(('', ''))

            # Escrevemos o título dos dados específicos de cada máquina
            writer.writerow(('Máquina', 'Peças com Sucesso', 'Peças falhas', 'Tempo médio de processamento (min)'))

            # Para cada máquina
            for i in range(self.ms):
                # Calculamos o número total de sucesso, falha e o tempo médio de processamento
                sucesso = self.sucesso[i]
                falha = self.falha[i]
                tempo = 60*self.t[i]/(sucesso+falha)

                # Escrevemos esses dados na tabel
                writer.writerow((i+1, sucesso, falha, tempo))

            # Escrevemos uma linha vazia
            writer.writerow(('', ''))
           

if __name__ == '__main__':
    # Dados do problema
    n_maq = 3 # Número de máquinas
    h_dia = 18 # Número de horas no dia
    p_hora = 60 # Número de peças por hora
    t_min = 2/60 # Tempo mínimo de processamento em horas
    t_max = 7/60 # Tempo máximo de processamento em horas
    p_sucesso = 80 # Probabilidade de sucesso na produção da peça
 
    # Objeto registrador de dados
    r = Registradora(n_maq)

    # Objeto gerador de produtos
    g = Gera(p_hora, h_dia, r)

    # Cria cada uma das máquinas
    for i in range(n_maq):
        Máquina(t_min, t_max, p_sucesso, i, r).start()
    
    # Tempo de inicio da fábrica
    t0 = time.time()

    # Inicia classe geradora
    g.start()

    # Espera o dia acabar
    while time.time() - t0 < h_dia: pass

    # Espera a classe geradora terminar
    g.join()

    # Registra os dados
    r.registra()


        
        
