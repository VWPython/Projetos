import random

from Personagem import Personagem

class inimigo(Personagem):
    def __init__(self, nome, FOR, DEF, HP, SP, ATKS, num = 0):
        self.num = num
        super(inimigo, self).__init__(nome, FOR, DEF, HP, SP, ATKS)

    def EscolheAtk(self):
        while True:
            atk = random.choice(self.ATKS)

            if self.SP >= Personagem.ATKS_GERAL[atk][1]:
                return atk

    def copy(self):
        return inimigo(self.nome, self.FOR, self.DEF, self.HP, self.SP, self.ATKS, self.num)

    def __str__(self):
        return '%i - %s com HP = %.2f e SP = %.2f'%(self.num, self.nome, self.HP, self.SP)
