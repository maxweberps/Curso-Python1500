"""
2) Faça um programa que imprima os n primeiros múltiplos de 5, sendo n definido
pelo usuário. Ex: Se o usuário escolheu n=3, será impresso 5,10,15.
"""

n = int(input('Digite um número: '))

for i in range(1, n + 1):
    print(f'5 x {i} = {5 * i}')
