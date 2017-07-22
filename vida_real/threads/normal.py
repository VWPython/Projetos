def roda():    
    with open('num.txt') as arq:
        print(sum([int(l.rstrip()) for l in arq]))
