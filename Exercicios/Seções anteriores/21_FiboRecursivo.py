'''
1 - Criar uma função recursiva (que retorne ela mesma) para armazenar N
termos da sequência de Fibonacci em uma lista. N é definido pelo usuário. Ao
encontrar os termos, imprimir a lista e finalizar a função.
'''

# cria lista e variável de parada
lista_termos = []
stop = 0


# função recusiva que gera os termos da seq. fibonacci
def fibonacci_rec(stop, a, b, aux):
    global lista_termos
    lista_termos.append(a)
    a, b = b, a + b
    aux += 1
    if stop == aux:
        print(lista_termos)
        return 0
    else:
        return fibonacci_rec(stop, a, b, aux)


# so aceita condição de parada se for maior que 0
while stop < 1:
    stop = int(input('Quantos termos da seq. Fibonacci deseja gerar? R: '))

# chama função fibonacci recursiva
fibonacci_rec(stop, a=1, b=1, aux=0)
