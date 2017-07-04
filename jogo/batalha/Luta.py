import random
from Personagem import Personagem

import shelve

class Luta(object):
    def __init__(self, player, inimigos):
        self.player = player
        self.CriaInimigos(inimigos)

    def main(self):
        #Depois iniciamos o combate
        while True:
            #Imprimimos as informações do player
            print(self.player)
            
            #Garantimos que o player vá escolher uma opção válida de atk
            while True:
                atk = self.menuCombate()
                if self.veSeAtkEhValido(atk):
                    break
                else:
                    print('Ataque não pode ser realizado, escolha novamente.')

            #Depois pedimos para o player escolher um alvo
            alvo = self.EscolheAlvo()

            #Tendo escolhido o alvo nós o isolamos do resto do grupo
            for inimigo in self.adversarios:
                if inimigo.num == alvo:
                    break

            #Então nós realizamos o atk do player
            self.player.atk(atk, inimigo)

            #Depois precisamos verificar se o inimigo morreu
            if inimigo.HP <= 0:
                self.adversarios.remove(inimigo)

            #Se o inimigo tiver morrido nós o removemos da lista de inimigos
            if len(self.adversarios) == 0:
                venceu = True
                break
            #Caso contrário iniciaremos o atk dos inimigos
            else:
                self.ataqueInimigos()

                #Então temos que verificar se o player perdeu ou não
                if self.player.HP == 0:
                    venceu = False
                    break

        #Depois do jogo vemos se o player venceu ou perdeu
        if venceu:
            print('\nParabens Você VENCEU!\n')
            #Se venceu ele pode restaurar se status ou aumentar atributos
            self.Venceu()

            self.player.InimigosMortos += 1

        else:
            print('Você sobreviveu a %i combates'%(self.player.InimigosMortos))
            print('Obrigado por jogar')
   
        

    def CriaInimigos(self, inimigos):
        """
        Método usada para criar os inimigos de um determinado combate
        """
        #Primeiro nós selecionamos o número de inimigos
        num_de_inimigos = 2**(self.player.InimigosMortos//10)

        #Depois criamos uma lista contendo todos os inimigos possiveis
        self.adversarios = []

        #Então sorteamos os inimigos e damos um número a cada um deles
        for i in range(num_de_inimigos):
            inimigo = random.choice(inimigos)
            inimigo.num = i+1
            self.adversarios.append(inimigo.copy())


    def menuCombate(self):
        """
        Função criada para escolher as opções do
        player
        """
        while True:
            saida = 'Deseja usar '
            for atk in self.player.ATKS:
                saida += atk + ', '

            saida = saida[:len(saida)-len(', ')]
            saida += ' ou deseja salvar o jogo?\n'
            comando = input(saida).lower()

            if not comando.isalpha():
                print('Digite apenas letra!')
            elif comando.startswith('s'):
                self.Salvar()
            else:
                for atk in self.player.ATKS:
                    if atk.lower()[0] == comando[0]:
                        return atk

                print('Não entendi seu comando, por favor digite novamente.')

    def veSeAtkEhValido(self, atk):
        if self.player.SP >= Personagem.ATKS_GERAL[atk][1]:
            return True
        else:
            print('SP insuficiente')
            return False

    def EscolheAlvo(self):
        """
        Função usada para garantir que o player
        escolha um alvo adequado
        """
        while True:
            saida = 'Escolha um alvo dentre: \n'
            nums = []
            for inimigo in self.adversarios:
                print(inimigo)
                nums.append(inimigo.num)

            comando = input(saida)

            if not comando.isdigit():
                print('Digite o número do inimigo!')
            else:
                if int(comando) not in nums:
                    print('Digite um número de inimigo válido!')
                else:
                    return int(comando)

    def ataqueInimigos(self):
        for inimigo in self.adversarios:
            atk = inimigo.EscolheAtk()

            inimigo.atk(atk, self.player)


    def Venceu(self):
        """
        Método chamada para quando o player vence o jogo
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
                    self.player.HP = 500
                    self.player.SP = 100
                    return
                #Se escolher aumentar chamos a função de aumentar os atributos
                elif comando.startswith('a'):
                    self.player.aumentaAtributo()
                    return
                #Caso contrário devolvemos uma mensagem de erro
                else:
                    print('Não entendi seu comando')

    def Salvar(self):
        arq = shelve.open('jogo.save')
        arq['Combate'] = True
        arq['Player'] = self.player
        arq['Adversários'] = self.adversarios
        arq.close()

    def Carregar(self, arq):
        self.player = arq['Player']
        self.adversarios = arq['Adversários']
        for adv in self.adversarios:
            print(adv)

        arq.close()
        
        self.main()

if __name__ == '__main__':
    from player import player
    from inimigo import inimigo

    Ogro = inimigo('Ogro', 30, 5, 100, 5, ['Clavada'])
    Goblin = inimigo('Goblin', 15, 10, 70, 30, ['Espadada', 'Flexada'])
    Esqueleto = inimigo('Esqueleto', 20, 20, 80, 20, ['Espadada', 'Cura'])
    Bruxo = inimigo('Bruxo', 10, 30, 80, 100, ['Relampago', 'BolaDeFogo', 'Espadada', 'Cura'])

    inimigos = [Ogro, Goblin, Esqueleto, Bruxo]

    Luta(player('Player'), inimigos).main()
