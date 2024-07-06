def primos_list(lista):
    for item in lista:
        divisor = 1
        numero_divisores = 0
        while divisor <= item:
            if item % divisor == 0:
                numero_divisores += 1
            divisor += 1
        if numero_divisores == 2:
            yield item


lista = []
sair = 'n'
while sair != 's':
    try:
        lista.append(int(input('Número: ')))
    except ValueError:
        print('Você deve digitar um número inteiro.')
    sair = input('deseja parar? s/n: ')

# objeto do tipo generator
print(primos_list(lista))
# convertendo o objeto para tupla
print(f'Números primos: {tuple(primos_list(lista))}')
