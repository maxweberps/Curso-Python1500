'''
1) Faça uma função que receba um número inteiro maior que zero e retorne a
soma de todos os algarismos.
Caso o valor seja negativo retorne 'Numero invalido'
Exemplo:
251 = 2 + 5 + 1 = 8
'''


def somar_algarismos(num):
    # levanta a quantidade de algarismos o número possui
    divisor = 1
    qtd_algarismo = 0
    while True:
        if (num // divisor) == 0:
            break
        else:
            qtd_algarismo += 1
            divisor *= 10

    # realiza a soma dos algarimos
    soma = 0
    for valor in range(qtd_algarismo):
        soma += ((num // (10 ** valor)) % 10)
    return soma


num = int(input('Digite um número inteiro maior que zero: '))
if num < 1:
    print('Número inválido')
else:
    print(f'Resultado da soma dos algarismos: {somar_algarismos(num)}')
