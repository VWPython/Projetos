import random

class Personagem(object):
    __calc_dano = (lambda atacante, atacado, x: max((atacante.FOR - atacado.DEF/x)*random.random(), 1))
    ATKS_GERAL = {'Espadada': (1, 0), 'Clavada': (1,0), 'Flexada': (2, 2),
              'Relampago': (3,5), 'BolaDeFogo': (5,10), 'Lança de Gelo': (5,10),
                'Cura': (0, 10)}

    def __init__(self, nome, FOR, DEF, HP, SP, ATKS):
        assert HP > 0
        assert SP > 0
        assert FOR > 0
        assert DEF > 0
        self.nome = nome
        self.FOR = FOR
        self.DEF = DEF
        self.HP = HP
        self.SP = SP
        self.ATKS = ATKS

    def atk(self, atk, atacado):
        if atk == 'Cura':
            self.cura()
            return
        dano = Personagem.__calc_dano(self, atacado, Personagem.ATKS_GERAL[atk][0])
        atacado.HP -= dano
        self.SP -= Personagem.ATKS_GERAL[atk][1]
        print('%s usou %s em %s'%(self.nome, atk.upper(), atacado.nome))
        print('%s causou %.2f de dano!'%(self.nome,dano))

    def cura(self):
        self.HP += 10
        self.SP -= 10
        print('%s usou CURA'%(self.nome))
