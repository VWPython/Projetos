"""
Escreva um jogo de sobrevivência, no qual o player irá escolher entre
continuar, salvar e desistir.

CONTINUAR --> O jogo escolherá 1 entre 4 inimigos para lutar com o player,
SALVAR --> Salva o estado do player e o número de inimigos derrotados
DESISTIR --> Salva um arquivo de Score contendo o tanto de inimigos que o
player derrotou

O combate:
Cada personagem do jogo possuí os seguintes atributos:
Player --> For 20, Def 20, HP 500 e SP 100
Ogro --> For 30, Def 5, HP 100 e SP 5
Goblin --> For 15, Def 10, HP 70 e SP 10
Esqueleto --> For 20, Def 20, HP 80 e SP 20
Bruxo --> For 10, Def 30, HP 80 e SP 20

O jogador pode escolher entre os seguintes ataques:
Espadada, Flexada, Cura, Lança de Gelo

Já os inimigos
Ogro --> Clavada
Goblin --> Flexada
Esqueleto --> Espadada, Cura
Bruxo --> Relampago, Bola de Fogo, Espadada, Cura

A cada final de batalha o jogador pode escolher entre aumentar em 5 o valor
de um atributo ou recuperar todo HP ou recuperar todo SP

A cada 10 inimigos derrotados o número de inimigos em uma batalha dobra, e o
player os enfrenta SIMULTANEAMENTE

O calculo de dano é:
Espada --> max((For - Def)*random(0,1), 1) consumo de SP 0
Flexada --> max((For - Def/3)*random(0,1), 1) consumo de SP 2
Clavada --> max((For - Def/1)*random(0,1), 1) consumo de SP 0
Relampago --> max((For - Def/5)*random(0,1), 1) consumo de SP 5
BolaDeFogo --> max((For - Def/5)*random(0,1), 1) consumo de SP 10
LançaDeGelo --> max((For - Def/5)*random(0,1), 1) consumo de SP 10
Cura --> recupera 10 consumo de SP 10
"""

import random, shelve

from player import player
from inimigo import inimigo
from Luta import Luta

class Jogo(object):
    """
    Objeto do jogo
    """
    def __init__(self):
        """
        Construtor do objeto Jogo
        """
        self.player = None

        Ogro = inimigo('Ogro', 30, 5, 100, 5, ['Clavada'])
        Goblin = inimigo('Goblin', 15, 10, 70, 30, ['Espadada', 'Flexada'])
        Esqueleto = inimigo('Esqueleto', 20, 20, 80, 20, ['Espadada', 'Cura'])
        Bruxo = inimigo('Bruxo', 10, 30, 80, 100, ['Relampago', 'BolaDeFogo', 'Espadada', 'Cura'])

        self.inimigos = [Ogro, Goblin, Esqueleto, Bruxo]

        self.main()

    def main(self):
        """
        Método principal do jogo
        """
        while True:
            com = self.menuInicial()

            if com.startswith('c'):
                self.carregaJogo()
            elif com.startswith('s'):
                break
            else:
                self.novoJogo()

    def jogando(self):
        while True:
            com = self.menuJogo()

            if com.startswith('c'):
                Luta(self.player, self.inimigos).main()
            elif com.startswith('s'):
                self.Salvar()
            else:
                break

    def menuInicial(self):
        """
        Pede para o usuário digitar o que ele deseja fazer inicialmente
        e devolve uma entrada válida
        """
        while True:
            comando = input('Deseja iniciar novo jogo(n/novo), carregar um jogo(c/carregar) ou sair(s/sair)?\n').lower()

            if not comando.isalpha():
                print('Digite apenas letra!')
            else:
                if comando.startswith('c') or comando.startswith('n') or comando.startswith('s'):
                    return comando
                else:
                    print('Não entendi seu comando digite novamente.')

    def carregaJogo(self):
        """
        Carrega um jogo salvo
        """
        try:
            arq = shelve.open('jogo.save')
        except IOError:
            print('Não há nenhum jogo salvo!')
        else:
            if arq['Combate']:
                Luta(player('player'), self.inimigos).Carregar(arq)
            else:
                self.player = arq['Player']
            arq.close()

    def novoJogo(self):
        """
        Cria um novo jogo e de as explicações básicas para o jogador
        """
        nome = input('Digite seu nome\n')
        self.player = player(nome)
        print('Bom %s, o jogo é simples\n'%nome)
        print('A cada rodada você pode escolher entre salvar o jogo, entrar em combate ou sair')
        print('Uma vez que você entre em combate terá de enfrentar inimigos')
        print('Se morrer acabou pra você')
        print('Se você sobreviver poderá escolher aumentar os atributos do seu personagem ou se curar')
        print('A cada 10 inimigos vencidos o número de inimigos a enfrentar dobra')
        print('Boa sorte\n')
        self.jogando()

    def menuJogo(self):
        """
        Dá as opções para o player enquanto ele está jogando
        e garante que será devolvida uma entrada válida
        """
        while True:
            comando = input('Deseja salvar (s/salvar) enfrentar novo inimigo (c/combate) ou sair (e/exit)?\n').lower()

            if not comando.isalpha():
                print('Digite apenas letra!')
            else:
                if comando.startswith('c') or comando.startswith('s') or comando.startswith('e') :
                    return comando
                else:
                    print('Não entendi seu comando digite novamente.')

    def Salvar(self):
        """
        Salva o jogo atual
        """
        arq = shelve.open('jogo.save')
        arq['Player'] = self.player
        arq['Combate'] = False
        arq['Adversários'] = []
        arq.close()


if __name__ == '__main__':
    Jogo()
