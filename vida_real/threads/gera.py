import random
with open('num.txt', 'w') as arq:
    for i in range(1000000):
        arq.write(str(random.randint(0, 10)) + '\n')
