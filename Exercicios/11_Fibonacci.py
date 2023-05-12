sequencias = int(input('Quantas sequencias deseja? '))

anterior = 0
proximo = 1
qtdPrimo = 0
soma = 0

for i in range(0, sequencias):
    print(f'\n{proximo}')

    # enquanto nao tiver os 5 primeiros numeros primos, continua a verificação
    if qtdPrimo < 5:

        # calcula as divisoes e conta quantas vezes o resto foi 0
        cont = 1
        divisores = 0
        while cont <= proximo:
            if proximo % cont == 0:
                divisores += 1
                print(f'O número {cont} é divisor de {proximo}')
            cont += 1

        # decide se o número é primo ou não
        if divisores == 2:
            soma += proximo
            print(f'{proximo} é primo!')
            qtdPrimo += 1

    proximo = proximo + anterior
    anterior = proximo - anterior

print(f'\nA média dos número primos, com limite de até 5, é: {soma / qtdPrimo}')
