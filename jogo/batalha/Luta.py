import random

def Luta(player, inimigos):
    """
    Função que implementa o combate entre o player e os inimigos
    """
    #Primeiro nós selecionamos os adversários do player
    adversarios = CriaInimigos(player, inimigos)

    #Depois iniciamos o combate
    while True:
        #Imprimimos as informações do player
        printPlayerInfo(player)
        
        #Garantimos que o player vá escolher uma opção válida de atk
        while True:
            atk = menuCombate(player)
            if veSeAtkEhValido(atk, player):
                break
            else:
                print('Ataque não pode ser realizado, escolha novamente.')

        #Depois pedimos para o player escolher um alvo
        alvo = EscolheAlvo(adversarios)

        #Tendo escolhido o alvo nós o isolamos do resto do grupo
        for inimigo in adversarios:
            if inimigo['num'] == alvo:
                break

        #Então nós realizamos o atk do player
        player['ATKS'][atk]['Atk'](player, inimigo)

        #Depois precisamos verificar se o inimigo morreu
        if inimigo['HP'] <= 0:
            adversarios.remove(inimigo)

        #Se o inimigo tiver morrido nós o removemos da lista de inimigos
        if len(adversarios) == 0:
            venceu = True
            break
        #Caso contrário iniciaremos o atk dos inimigos
        else:
            ataqueInimigos(player, adversarios)

            #Então temos que verificar se o player perdeu ou não
            if player['HP'] == 0:
                venceu = False
                break

    #Depois do jogo vemos se o player venceu ou perdeu
    if venceu:
        print('\nParabens Você VENCEU!\n')
        #Se venceu ele pode restaurar se status ou aumentar atributos
        Venceu(player)

        player['Inimigos Mortos'] += 1

    else:
        print('Você sobreviveu a %i combates'%(player['Inimigos Mortos']))
        print('Obrigado por jogar')
        

def CriaInimigos(player, inimigos):
    """
    Função usada para criar os inimigos de um determinado combate
    """
    #Primeiro nós selecionamos o número de inimigos
    num_de_inimigos = 2**(player['Inimigos Mortos']//10)

    #Depois criamos uma lista contendo todos os inimigos possiveis
    adversarios = []

    #Então sorteamos os inimigos e damos um número a cada um deles
    for i in range(num_de_inimigos):
        inimigo = random.choice(inimigos)
        inimigo['num'] = i+1
        adversarios.append(inimigo.copy())

    return adversarios

def menuCombate(player):
    """
    Função criada para escolher as opções do
    player
    """
    while True:
        saida = 'Deseja usar '
        for key in player['ATKS']:
            saida += key + ', '

        saida = saida[:len(saida)-len(', ')] + '?\n'
        comando = input(saida).lower()

        if not comando.isalpha():
            print('Digite apenas letra!')
        else:
            for key in player['ATKS']:
                if key.lower()[0] == comando[0]:
                    return key

            print('Não entendi seu comando, por favor digite novamente.')

def veSeAtkEhValido(atk, player):
    if player['ATKS'][atk]['SP'] <= player['SP']:
        return True
    else:
        print('SP insuficiente')
        return False

def EscolheAlvo(adversarios):
    """
    Função usada para garantir que o player
    escolha um alvo adequado
    """
    while True:
        saida = 'Escolha um alvo dentre: \n'
        nums = []
        for inimigo in adversarios:
            saida += '%i - %s  HP = %.2f/ SP = %.2f\n'%(inimigo['num'], inimigo['Nome'], inimigo['HP'], inimigo['SP'])
            nums.append(inimigo['num'])

        comando = input(saida)

        if not comando.isdigit():
            print('Digite o número do inimigo!')
        else:
            if int(comando) not in nums:
                print('Digite um número de inimigo válido!')
            else:
                return int(comando)

def ataqueInimigos(player, adversarios):
    for inimigo in adversarios:
        atk = EscolheAtkInimigo(inimigo)

        inimigo['ATKS'][atk]['Atk'](inimigo, player)


def EscolheAtkInimigo(inimigo):
    while True:
        atk = random.choice(list(inimigo['ATKS'].keys()))

        if inimigo['SP'] >= inimigo['ATKS'][atk]['SP']:
            return atk

def printPlayerInfo(player):
    """
    Imprime as informações do player
    """
    print('HP: ', player['HP'])
    print('SP: ',player['SP'])
    print()

def Venceu(player):
    """
    Função chamada para quando o player vence o jogo
    """
    while True:
        #Primeiro nós vemos o que o player quer fazer
        comando = input('Deseja restaurar o status(r/restaurar) ou aumentar um atributo(a/aumentar)?\n').lower()

        #Temos que garantir que ele não enfiou nenhum caracter estranho no meio do comando
        if not comando.isalpha():
            print('Digite apenas letras!')
        else:
            #Se ele escolher restaurar aumentamos seu hp e sp
            if comando.startswith('r'):
                player['HP'] = 500
                player['SP'] = 100
                return
            #Se escolher aumentar chamos a função de aumentar os atributos
            elif comando.startswith('a'):
                aumentaAtributo(player)
                return
            #Caso contrário devolvemos uma mensagem de erro
            else:
                print('Não entendi seu comando')

def aumentaAtributo(player):
    """
    Permite que o player aumente o valor de um de seus atributos
    """
    while True:
        comando = input('Deseja aumentar a força(f/for) ou a defesa (d/def)?\n').lower()

        if not comando.isalpha():
            print('Digite apenas letras!')
        else:
            if comando.startswith('f'):
                player['For'] += 5
                break
            elif comando.startswith('d'):
                player['Def'] += 5
                break
        
        
            else:
                print('Não entendi seu comando')

    print('Player For: %i \nPlayer Def: %i'%(player['For'], player['Def']))
