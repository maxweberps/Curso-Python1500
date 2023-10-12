'''
Leia dois valores inteiros M e N indefinidamente. A cada leitura, calcule e escreva a soma dos fatoriais de cada um
dos valores lidos. Utilize uma variável apropriada, pois cálculo pode resultar em um valor com mais de 15 dígitos.
'''

m, n = int(input()), int(input())
fat_m, fat_n = 1, 1

for i in range(1, m + 1):
    fat_m *= i

for i in range(1, n + 1):
    fat_n *= i

print(fat_m+fat_n)