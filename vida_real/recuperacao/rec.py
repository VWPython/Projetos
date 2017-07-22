import os, sys

#Pegamos o diretório que contem os arquivos bagunçados
diretorio = sys.argv[1]

#Pegamos o nome do novo diretório a partir da primeira linha no arquivo
nome = input()

#Obtemos o caminho até o diretório recuperado
caminho = os.path.join(os.getcwd(), "Recuperação", nome)

#Criamos esse diretório
os.mkdir(caminho)

#Ajustamos o caminho até o novo diretório de acordo com o sistema operacional
if 'win' not in sys.platform:
    caminho = caminho.replace(" ", "\ ")
else:
    caminho = os.path.join(os.getcwd(), "Recuperação", '"'+nome+'"')
    

for (nome, sub, arqs) in os.walk(diretorio):
    #Percorremos todos os arquivos no diretorio bagunçado    
    for fnome in arqs:
        #Os copiamos para a nova pasta e removemos da pasta antiga
        if 'win' not in sys.platform:
            os.system("cp %s %s"%(os.path.join(nome, fnome), caminho))
            os.system("rm " + os.path.join(nome, fnome))
        else:
            os.system("copy %s %s"%(os.path.join(nome, fnome), caminho))
            os.system("DEL " + os.path.join(nome, fnome))
