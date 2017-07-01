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

import random

from Lutas import *


def main():
    """
    Função Principal do Jogo
    """

    calc_dano = (lambda atacante, atacado, x: max((atacante['For'] - atacado['Def']/x)*random.random(), 1))


    def Espadada(atacante, atacado):
        """
        Função que implementa o ataque de Espada
        """
        nonlocal calc_dano
        dano = calc_dano(atacante, atacado, 1)

        atacado['HP'] -= dano
        print('%s usou ESPADADA em %s'%(atacante['Nome'], atacado['Nome']))
        print('%s causou %.2f de dano!'%(atacante['Nome'],dano))

    def Flexada(atacante, atacado):
        """
        Função que implementa o ataque de Flexa
        """
        nonlocal calc_dano
        dano = calc_dano(atacante, atacado, 2)

        atacado['HP'] -= dano
        atacante['SP'] -= 2
        print('%s usou FLEXADA em %s'%(atacante['Nome'], atacado['Nome']))
        print('%s causou %.2f de dano!'%(atacante['Nome'],dano))

    def Clavada(atacante, atacado):
        """
        Função que implementa o ataque de Clava
        """
        nonlocal calc_dano
        dano = calc_dano(atacante, atacado, 1)

        atacado['HP'] -= dano
        print('%s usou Clavada em %s'%(atacante['Nome'], atacado['Nome']))
        print('%s causou %.2f de dano!'%(atacante['Nome'],dano))

    def Relampago(atacante, atacado):
        """
        Função que implementa o ataque de Relampago
        """
        nonlocal calc_dano
        dano = calc_dano(atacante, atacado, 3)

        atacado['HP'] -= dano
        atacante['SP'] -= 5
        print('%s usou RELAMPAGO em %s'%(atacante['Nome'], atacado['Nome']))
        print('%s causou %.2f de dano!'%(atacante['Nome'],dano))

    def BolaDeFogo(atacante, atacado):
        """
        Função que implementa o ataque de Bola de Fogo
        """
        nonlocal calc_dano
        dano = calc_dano(atacante, atacado, 5)

        atacado['HP'] -= dano
        atacante['SP'] -= 10
        print('%s usou BOLA DE FOGO em %s'%(atacante['Nome'], atacado['Nome']))
        print('%s causou %.2f de dano!'%(atacante['Nome'],dano))

    def LançaDeGelo(atacante, atacado):
        """
        Função que implementa o ataque de Lança de Gelo
        """
        nonlocal calc_dano
        dano = calc_dano(atacante, atacado, 5)

        atacado['HP'] -= dano
        atacante['SP'] -= 10
        print('%s usou LANÇA DE GELO em %s'%(atacante['Nome'], atacado['Nome']))
        print('%s causou %.2f de dano!'%(atacante['Nome'],dano))

    def Cura(usuário, default):
        """
        Função que implementa o ataque de Lança de Gelo
        """
        usuário['HP'] += 10
        usuário['SP'] -= 10
        print('%s usou CURA'%(usuário['Nome']))

    Player = {"Nome": 'Player',
              'For': 20, 'Def': 20, 'HP': 500, 'SP': 100,
              'ATKS': {'Espadada': {'Atk': Espadada, 'SP': 0}, 'Flexada': {'Atk': Flexada, 'SP': 2},
                       'Cura':{'Atk': Cura, 'SP': 10}, 'Lança de Gelo': {'Atk': LançaDeGelo, 'SP': 10}},
              'Inimigos Mortos': 0}

    Ogro = {'Nome': 'Ogro',
            'For': 30, 'Def': 5, 'HP': 100, 'SP': 5,
            'ATKS': {'Clavada': {'Atk': Clavada, 'SP': 0}}}

    Goblin = {'Nome': 'Goblin',
              'For': 15, 'Def': 10, 'HP':70, 'SP': 30,
              'ATKS': {'Espadada': {'Atk': Espadada, 'SP': 0}, 'Flexada': {'Atk': Flexada, 'SP': 2}}}

    Esqueleto = {'Nome': 'Esqueleto',
                 'For': 20, 'Def': 20, 'HP': 80, 'SP': 20,
                 'ATKS': {'Espadada': {'Atk': Espadada, 'SP': 0}, 'Cura':{'Atk': Cura, 'SP': 10}}}

    Bruxo = {'Nome': 'Bruxo',
             'For': 10, 'Def': 30, 'HP': 80, 'SP': 100,
             'ATKS': {'Relampago': {'Atk': Relampago, 'SP': 5}, 'BolaDeFogo': {'Atk': BolaDeFogo, 'SP': 10}, 'Cura':{'Atk': Cura, 'SP': 10},
                      'Espadada': {'Atk': Espadada, 'SP': 0}}
             }

    Inimigos = [Ogro, Goblin, Esqueleto, Bruxo]

    while True:
        com = menuInicial()

        if com.startswith('c'):
            carregaJogo(Player)
        elif com.startswith('s'):
            break
        else:
            novoJogo(Player)

        while True:
            com = menuJogo()

            if com.startswith('c'):
                CriaInimigosLuta(Player, Inimigos)
            elif com.startswith('s'):
                Salvar(Player)
            else:
                break

def menuInicial():
    while True:
        comando = input('Deseja iniciar novo jogo(n/novo), carregar um jogo(c/carregar) ou sair(s/sair)?\n').lower()

        if not comando.isalpha():
            print('Digite apenas letra!')
        else:
            if comando.startswith('c') or comando.startswith('n') or comando.startswith('s'):
                return comando
            else:
                print('Não entendi seu comando digite novamente.')

def carregaJogo(player):
    pass

def novoJogo(player):
    player['Nome'] = input('Digite seu nome\n')
    print('Bom %s, o jogo é simples\n'%player['Nome'])
    print('A cada rodada você pode escolher entre salvar o jogo, entrar em combate ou sair')
    print('Uma vez que você entre em combate terá de enfrentar inimigos')
    print('Se morrer acabou pra você')
    print('Se você sobreviver poderá escolher aumentar os atributos do seu personagem ou se curar')
    print('A cada 10 inimigos vencidos o número de inimigos a enfrentar dobra')
    print('Boa sorte\n')

def menuJogo():
    while True:
        comando = input('Deseja salvar (s/salvar) enfrentar novo inimigo (c/combate) ou sair (e/exit)?\n').lower()

        if not comando.isalpha():
            print('Digite apenas letra!')
        else:
            if comando.startswith('c') or comando.startswith('s') or comando.startswith('e') :
                return comando
            else:
                print('Não entendi seu comando digite novamente.')

def Salvar(player):
    pass

main()
