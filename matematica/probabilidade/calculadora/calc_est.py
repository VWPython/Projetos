from tkinter import *
from functools import partial
from est import *

class Calculadora(object):
    def __init__(self, toplevel):
        """
        Método construtor da classe bagels. Recebe
        uma toplevel criada a partir do modulo
        tkinker que contem a app
        """

        #Criamos uma tupla confiurando uma fonte 1
        self.font1 = ('Verdana', '14', 'bold')

        #Váriavel que contem a tupla com as configurações da fonte
        self.font2 = ('Verdana', '10', 'bold')

        self.criaFrames(toplevel)
        self.criaEntrys()
        self.criaLabels()
        self.criaBotões()


    def criaFrames(self, toplevel):
        #Essa frame conterá os modos de cálculo a utilizar
        self.frame1 = Frame(toplevel, height = 50, pady = 10)


        #Essa frame contem a caixa de texto onde
        #serão colocados as fórmulas e funções
        self.frame2 = Frame(toplevel)

        #Coloca um botão mandando fazer o cálculo
        self.frame3 = Frame(toplevel)
 
        #Frame onde serão colocadas instruções de
        #cada função e as entradas especiais
        self.frame4 = Frame(toplevel, height = 0, pady = 0)

        #Frame onde serão colocados os botões especiais
        self.frame5 = LabelFrame(toplevel)

        #Por fim empacotamos todas as frames
        self.frame1.pack(side = TOP)
        self.frame2.pack(side = TOP)
        self.frame3.pack(side = TOP)
        self.frame4.pack(side = TOP)
        self.frame5.pack(side = TOP)

    def criaBotões(self):
        """
        Cria os botões do programa
        """

        #Colocamos os botões dos modos especiais
        self.bino_atv = False
        self.bino = Checkbutton(self.frame1, font = self.font2, text = 'Modo Binomial',
                            bg = 'lightgray', command = self.AtvBino)
        self.bino.pack(side = LEFT)

        self.pois_atv = False
        self.poisson = Checkbutton(self.frame1, font = self.font2, text = 'Modo Poisson',
                            bg = 'lightgray', command = self.AtvPoisson)
        self.poisson.pack(side = RIGHT)

        #Colocamos o botão que manda o calculo
        self.go = Button(self.frame3, font = self.font2, text = 'Calcule',
                            bg = 'lightgray', command = self.GO)
        self.go.pack()

        ##### Colocamos os botões especiais #####
        botões = ('Comb(n, k)', 'binomial(n, x, p)', 'poisson(l, x, t)', 'soma(n, p, maior, menor = 0)', 'media', 'desvio', 'moda', 'mediana', 'variancia', 'p(x > k)', 'p(x >= k)', 'p(x < k)', 'p(x <= k)', 'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)', 'p(k1 <= x <= k2)')
        
        #Vamos armazenar as subframes do frame5 numa lista
        self.subFrames = []
        
        #Vamos percorrer todos os botões
        for i in range(len(botões)):
            #Vamos utilizar apenas 3 botões por linha
            if i % 3 == 0:
                #Criamos a subframe
                subframe = Frame(self.frame5)
                subframe.pack(side = TOP)
                currentFrame = subframe
                self.subFrames.append(subframe)
            
            #E o botão
            b = Button(currentFrame, font = self.font2, text = botões[i],
                            bg = 'green', command = partial(self.Especial, botões[i]), width=25)
            b.pack(side=LEFT)

        #E por fim colocamos o botão de delete
        b = Button(currentFrame, font = self.font2, text = 'del', bg = 'red', command = self.Del, width=25)
        b.pack(side=RIGHT)

    def criaEntrys(self):
        """
        Coloca as entrys do programa
        """
        #Colocamos na frame 2 a nossa entrada da formula
        self.form = Entry(self.frame2, width=50, font=self.font2)
        #Colocamos ela do lado esquerdo do frame
        self.form.pack(side = LEFT)

    def criaLabels(self):
        """
        Cria os labels do programa
        """
        #Criamos o texto que será divulgado para o usuário sobre o uso de cada
        #função
        self.msg = Label(self.frame4, text = '',
                         font = self.font1)
        self.msg.pack()

    def constroiEspecial(self, n, p):
        """
        Contrói os campos para colocar informações referentes aos modos
        binomial e poisson
        """
        self.n_text = Label(self.frame4, text = '%s = '%n, font = self.font1)
        self.n_text.pack(side = LEFT)
        self.n = Entry(self.frame4, width=5, font=self.font2)
        self.n.pack(side = LEFT)

        self.p = Entry(self.frame4, width=5, font=self.font2)
        self.p.pack(side = RIGHT)
        self.p_text = Label(self.frame4, text = '%s = '%p, font = self.font1)
        self.p_text.pack(side = RIGHT)

    def AtvBino(self):
        """
        Ativa o modo binomial
        """

        if not self.bino_atv:
            #Primeiro nós mudamos a várivel que retem se o modo está ativado
            self.bino_atv = True
            if self.pois_atv:
                #Se um dos modos já foi ativado basta trocar o texto
                self.n_text['text'] = 'n = '
                self.p_text['text'] = 'p = '
                self.pois_atv = False
                self.poisson.deselect()
                
            else:
                #Depois nós inserimos os campos especiais
                self.constroiEspecial('n', 'p')
        else:
            #Se não estiver ativado nós destruimos
            self.destroi()

    def AtvPoisson(self):
        """
        Ativa o modo Poisson
        """
        if not self.pois_atv:
            #Primeiro nós mudamos a várivel que retem se o modo está ativado
            self.pois_atv = True
            
            if self.bino_atv:
                self.n_text['text'] = 'l = '
                self.p_text['text'] = 't = '
                self.bino_atv = False
                self.bino.deselect()

            else:
                #Depois nós inserimos os campos especiais
                self.constroiEspecial('n', 'l')

                
        else:
            self.destroi()

    def destroi(self):
        """
        Destrói os botões criados nos modos especiais
        """
        self.n.destroy()
        self.n_text.destroy()
        self.p.destroy()
        self.p_text.destroy()
        self.bino_atv = False
        

    def Especial(self, nome):
        """
        Insere um conteúdo especial na entrada de fórmula
        """
        self.form.insert(END, nome)

    def Del(self):
        """
        Deleta todo o texto contido no campo de fórmulas
        """
        self.form.delete(0, END)

    def devolveResultado(self, valor):
        """
        Coloca a mensagem indicando o resultado da operação
        """
        self.msg['text'] = self.form.get() + ' = ' + str(valor)
        self.msg['fg'] = 'blue'
        self.Del()

    def erro(self, msg):
        """
        Coloca uma mensagem de erro na tela
        """
        self.msg['text'] = msg
        self.msg['fg'] = 'red'

    def devolveResultado(self, op, valor):
        """
        Devolve uma mensagem com o resultado da operação
        """
        self.msg['text'] = op + ' = ' + str(valor)
        self.msg['fg'] = 'blue'

    def recebe_N_e_P(self):
        """
        Pega os valor de n e p, ou no caso de poisson
        l e t
        """
        try:
            n = int(self.n.get())
            p = float(self.p.get())
            return n, p
        except ValueError:
            self.erro('Parâmetros Inválidos')
            return None, None
 
    def calcula(self, texto, func, *extras):
        n, p = self.recebe_N_e_P()
        if n != None and p!= None:
            if len(extras) > 0:
                self.devolveResultado(texto, func(n, p, *extras))
            else:
                self.devolveResultado(texto, func(n, p, *extras))
    
    def AchaFuncNome(self, nome):
         """
         Acha o nome da função indicada
         """
         x = 0
         for l in nome:
             if l == '(':
                 break
             x += 1
         return nome[0:x]

    def pegaParametros(self, texto):
        sem_esp = texto.replace(" ", "")
        nome = self.AchaFuncNome(sem_esp)
        sem_nome = sem_esp[len(nome):len(texto)]
        sem_conc = sem_nome.replace("(", "").replace(")", "")
        return sem_conc
    
    def calculaSoma(self, texto, func):
        params = self.pegaParametros(texto)
        n, p = self.recebe_N_e_P()
        if n != None and p!= None:
            separado = params.split(',')
            if len(separado) != 3 and len(separado) != 4:
                self.erro('Parâmetros Inválidos')
                return
            try:
                maior = int(separado[2])
            except ValueError:
                self.erro('Parâmetros Inválidos')
                return 

            if len(separado) == 4:
                try:
                    menor = int(separado[3])
                except ValueError:
                    self.erro('Parâmetros Inválidos')
                    return
            else:
                menor = 0
                    
            self.devolveResultado(texto, soma(n, p, func, maior, menor))
    
    def GO(self):
        """
        Realiza operações e verificações quanto ao que foi colocado
        no campo de fórmula
        """
        
        #Funções que são específicas para cada distribuição
        especifico = {'desvio': [desvioBinomial, desvioPoisson], 'variancia': [varianciaBinomial, varianciaPoisson], 'moda': [modaBinomial, modaPoisson]}
        
        exp1 = ['media', 'mediana', 'soma(n, p, maior, menor = 0)']
        #exp2 = {'p(x > k)': pMaior, 'p(x >= k)': pMaiorIgual, 'p(x < k)': pMenor, 'p(x <= k)': pMenorIgual}
        #exp3 = ['p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)', 'p(k1 <= x <= k2)']
        
        #Obtemos o que foi colocado pelo usuário
        texto = self.form.get()
        
        #Verificamos primeiro se trata da média
        if self.bino_atv or self.pois_atv:
            if texto == 'media':
                self.calcula(texto, media)
                return
                
        
        #Verificamos se a dependência entre um dos modos
        if self.bino_atv:
            if texto in especifico:
                self.calcula(texto, especifico[texto][0])

            elif texto == 'mediana':
                self.calcula(texto, mediana, binomial)
            elif self.AchaFuncNome(texto) == 'soma':
                self.calculaSoma(texto, binomial)

        elif self.pois_atv:
            if texto in especifico:
                self.calcula(texto, especifico[texto][1])

            elif texto == 'mediana':
                self.calcula(texto, mediana, poisson)
            elif self.AchaFuncNome(texto) == 'soma':
                self.calculaSoma(texto, poisson)
        
        else:
            try:
                valor = eval(texto)
                self.devolveResultado(texto, valor)
            except SyntaxError:
                self.erro('Entrada Inválida')
            except NameError:
                self.erro('Parâmetros Inválidos')
                  

              
                

        

instancia = Tk()
Calculadora(instancia)
instancia.title('Calculadora para Estatística')
instancia.geometry("800x600")
instancia.mainloop()
