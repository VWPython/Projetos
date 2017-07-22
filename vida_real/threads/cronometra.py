import timeit

setup = open('gab.py').read()
print(min(timeit.Timer('roda()', setup=setup).repeat(1, 10)))

setup = open('normal.py').read()
print(min(timeit.Timer('roda()', setup=setup).repeat(1, 10)))
