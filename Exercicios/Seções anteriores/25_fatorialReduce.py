'''
1 - Calcule fatorial de N utilizando loop for e depois reduce. o resultado é o mesmo?
'''
from functools import reduce

n = int(input('Fator de: '))
fat = 1

for i in range(1, n + 1):
    fat *= i
print(f'Fatorial de {n}: {fat}')

# COM REDUCE
lista = [1]
lista.extend(range(1, n + 1))
fat = reduce(lambda x, y: x * y, lista)
print(f'Fatoral de {n} com reduce: {fat}')
