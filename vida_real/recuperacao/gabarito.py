import os, sys

def main():
    """
    Função principal do programa
    """

    #Primeiro vamos pegar o diretório padrão
    cwd = os.getcwd()

    #Vamos criar o diretório de recuperação
    try:
        os.mkdir("Recuperação")
    except FileExistsError:
        os.rmdir("Recuperação")
        os.mkdir("Recuperação")

    #Salvemos também o caminho absoluto para o diretório
    #de recuperação
    rec = os.path.abspath("Recuperação")

    #Ok, agora vamos começar a percorrer os diretórios contidos
    #dentro de found.000, vamos fazer isso usando o os.walk
    for (nome, sub, arqs) in os.walk(os.path.join(cwd, "found.000")):
        #Vamos procurar dentro do diretório o arquivo
        #Descrição.txt
        for fnome in arqs:
            if fnome == "Descrição.txt":
                #Salvemos o caminho para descrição.txt
                caminho = os.path.join(nome, fnome)

                #Usemos o arquivo de descrição para executar o script
                #de recuperação de informações do diretório
                if "win" in sys.platform:
                    os.system("python %s < %s %s"%(os.path.join(cwd, "rec.py"), caminho, nome))
                else:
                    os.system("python3 %s < %s %s"%(os.path.join(cwd, "rec.py"), caminho, nome))

                
                #Uma vez recuperados podemos sair desse diretório e passar
                #para o próximo
                break

         
        #Depois nós apagamos o diretório
        try:
            os.rmdir(nome)
        except OSError:
            continue

    #Por fim removemos o diretório superior
    os.rmdir("found.000")

if __name__ == "__main__":
    main()
