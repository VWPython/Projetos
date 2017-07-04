#Estatistica

from math import factorial as fac
from math import e
import functools

##### Binomial #####

def binomial(n, x, p):
    """
    Distribuição probabilística binomial, para n elementos
    um número x de casos favoráveis e a probabilidade de cada
    caso
    """
    return Comb(n,x)*(p**x)*((1-p)**(n-x))

def desvioBinomial(n, p):
    """
    Cálcula o desvio padrão de uma distribuição
    binomial
    """
    return n*p*(1-p)

def varianciaBinomial(n,p):
    """
    Calcula a variância para uma distribuição binomial
    """
    return desvioBinomial(n, p)**2

def modaBinomial(n, p):
    """
    Calcula a moda de uma determinada distribuição
    NO CASO DE POISSON ENTENDE-SE N=T E P=L
    """
    return functools.reduce(max, (binomial(n,x,p) for x in range(n+1)))


######## POISSON #############

def poisson(l, x, t):
    """
    Distribuição probabilística de poisson, para um
    lambda l, com um número t para um número x de casos favoráveis
    caso
    """
    return (e**(-l*t))*((l*t)**x)/fac(x)


def desvioPoisson(l, t):
    """
    Cálcula o desvio padrão de uma distribuição
    poisson
    """
    return t*l

def varianciaPoisson(l, t):
    return desvioPoisson(l, t)**2    

def modaPoisson(n, p):
    """
    Calcula a moda de uma determinada distribuição
    NO CASO DE POISSON ENTENDE-SE N=T E P=L
    """
    return functools.reduce(max, (binomial(n,x,p) for x in range(n+1)))

###########################################################################

def media(n, p):
    """
    Calcula o valor médio para uma distribuição binomial
    de n com probabilidade favorável p
    NO CASO DE POISSON ENTENDE-SE N=T E P=L
    """
    return n*p

def mediana(n, p, func):
    soma = 0
    x = 0
    while soma < 0.5:
        soma += func(n, x, p)
        x += 1
    
    return x if soma != 0.5 else x-1

def soma(n, p, func, maior, menor = 0):
    """
    Soma das probabilidades calculadas por meio de
    uma distribuição binomial indo de x = menor
    até x = maior. Recebe o número n de fatores
    e a probabilidade de sucesso p
    PARA poisson entende-se n = l e p = t
    """
    return sum((func(n,x,p) for x in range(menor, maior+1)))

def retira(n, p, m, func):
    return 1 - sum([func(p,x,n) for x in range(m+1)])

def pMaiorIgual(n, p, m, func):
    return 1 - sum((func(n,x,p) for x in range(m+1)))

def pMaior(n, p, m, func):
    return 1 - sum((func(n,x,p) for x in range(m)))

def Comb(n, k):
    """
    Combinações de n elementos em k agrupamentos
    """
    return fac(n)/(fac(k)*fac(n-k))
    

#retiraBinomial = (lambda m,p: 1 - somaBinomial(m,p))

#retiraPoisson = (lambda l,t,n: 1 - sum([poisson(l,t,k) for k in range(n+1)]))

