'''
1 - Receba numeros inteiros do usuário e armazene-os em uma lista. Crie uma
condição para o número 0 finalizar o processo de preenchimento. Após isso,
imprima o maior valor da lista utilizando as funções sorted() e len(). Por fim,
utilize reversed() para inverter a lista e obtenha, pelo índice, o valor
intermediário da mesma.
Obs.: Caso o número de valores da lista seja par, pegue a média dos dois
valores centrais.
'''
numeros = []
print('adicionar numeros a lista\npara encerrar digite 0')
while True:
    num = int(input('digite um numero: '))
    if num == 0:
        break
    else:
        numeros.append(num)

print('-------------')
print(f'Lista criada: {numeros}')
ordenados = sorted(numeros)
tamanho = len(numeros)
print(f'O maior numero da lista é: {ordenados[tamanho - 1]}')
print(f'Lista ordenada: {ordenados}')
print(f'Lista invertida: {list(reversed(numeros))}')
if len(numeros) % 2 == 0:
    print(
        f'Média dos valores intermediários: {(ordenados[tamanho // 2 - 1] + ordenados[tamanho // 2]) / 2}')
else:
    print(f'Valor intermediário: {ordenados[tamanho // 2]}')
