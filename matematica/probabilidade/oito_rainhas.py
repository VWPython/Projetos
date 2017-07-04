"""
Você deve resolver o clássico exercício das 8 rainhas
Nele o usuário lhe passa o tamanho do tabuleiro n
(lembrar que tabuleiros são quadrados então o usuário
só precisa lhe passar um inteiro) e você deve gerar
uma todas as distribuições de n rainhas neste tabuleiro
e imprimi-las de uma forma adequada.

Veja o livro Beginning Python, na descrição
do video para a explicação da solução, ou entre
no dropbox para ver a solução comentada

Esse exercício não é fácil!!
Não se preocupe se você não conseguir
"""

def main():
    num = int(input("Digite o tamanho do tabuleiro: "))
    soluções = list(rainhas(num, ()))
    for sol in range(len(soluções)):
        print("##### SOLUÇÃO %.2i #####"%(sol+1))
        imprimeTab(soluções[sol])
        print()

def conflito(tab, proxX):
    """
    Função que retorna um valor booleano
    dizendo se há ou não um conflito
    gerado a partir da colocação de uma
    rainha na coluna proxX numa linha
    proxY qualquer
    """
    #Primeiro nós vemos qual é a próxima linha
    proxY = len(tab)
    
    #Depois percorremos cada uma das posições nesta
    #linha e vemos se ela é afetada pelas outras damas
    for i in range(proxY):
        #Nota abs == modulo do número
        #Depois nós verificamos se há algum conflito
        
	#O conflito ocorre se as duas damas estiverem na mesma linha
	#abs(tab[i]-proxX) == 0
        
	#Ou na mesma diagonal
        #abs(tab[i]-proxX) == proxY-i
        if abs(tab[i]-proxX) in (0, proxY-i):
            return True
    #Caso a posição não gere conflito nós retornamos falso
    return False

def rainhas(num, tab):
    """
    Função que retorna todas as posições possíveis
    para as rainhas num determinado tabuleiro de
    tamanho num
    """
    #Primeiro olhamos todas as posições numa determinada coluna
    for pos in range(num):
        #Se a posição não gerar conflito significa
        #que ela é umas das possíveis e deve ser retornada
        if not conflito(tab, pos):
            #Se estamos tratando da última rainha significa
            #que podemos simplesmente retornar a posição
            if len(tab) == num-1:
                yield (pos,)
            else:
                #Caso contrário usaremos recursividade --> rainhas(num, tab + (pos,))
                #desta forma iremos ir chamando o nosso gerador
                
                #A cada iteração adicionaremos a pos que não gera conflito --> tab + (pos,)
                
                #Quando chegarmos na última posição teremos retorno da última posição
                #Basta somarmos está ao resto da nossa tupla
                #que teremos um tupla completa --> (pos, ) resultado
                
                #Tambem funciona para resultados vazios, pois reinicia 
                #a sequência testando novos valores
                for resultado in rainhas(num, tab + (pos,)):
                    yield (pos,) + resultado

def imprimeTab(sol):
    def linha(pos, tamanho=len(sol)):
        return '. ' * (pos) + 'X ' + '. ' * (tamanho-pos-1)
    for pos in sol:
        print (linha(pos))
                
main()
