from Personagem import Personagem

class player(Personagem):
    def __init__(self, nome):
        HP = 500
        SP = 100
        FOR = 20
        DEF = 20
        ATKS = ['Espadada', 'Flexada', 'Cura', 'Lança de Gelo']
        super(player, self).__init__(nome, FOR, DEF, HP, SP, ATKS)
        self.InimigosMortos = 0

    def aumentaAtributo(self):
        """
        Permite que o player aumente o valor de um de seus atributos
        """
        while True:
            comando = input('Deseja aumentar a força(f/for) ou a defesa (d/def)?\n').lower()

            if not comando.isalpha():
                print('Digite apenas letras!')
            else:
                if comando.startswith('f'):
                    self.FOR += 5
                    break
                elif comando.startswith('d'):
                    self.DEF += 5
                    break
                else:
                    print('Não entendi seu comando')

        print('%s For: %i \nPlayer Def: %i'%(self.nome,self.FOR, self.DEF))

    def __str__(self):
        return 'HP: %s\nSP: %s\n\n'%(self.HP, self.SP)
