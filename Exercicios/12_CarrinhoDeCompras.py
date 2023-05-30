"""
1 - Crie duas listas, uma para o carrinho do supermercado que irá receber
produtos comprados e outra para os preços dos produtos. Utilizando um loop,
preencha as listas com 5 produtos e 5 preços, recebendo estes dados do
usuário (input). Por fim, some os preços, imprima o valor total e os produtos do
carrinho.
"""

opcao = 1
listaNome = []
listaPreco = []

print('CARRINHO DE COMPRAS')

while True:
    opcao = int(input('Deseja adicionar um item ao carrinho? (1 - Sim) (2 - Não) R: '))

    if opcao == 1:
        i = 0
        listaNome.insert(i, input('Nome: '))
        listaPreco.insert(i, float(input('Preço: ')))
        i = i + 1
    elif opcao == 2:
        break
    else:
        print('Opção inválida! Tente novamente')

print('RESUMO DA COMPRA: ')
valorTotal = 0
for elemento in range(0, len(listaPreco)):
    valorTotal += listaPreco[elemento]
    print(f'{listaNome[elemento]}....{listaPreco[elemento]}')
print(f'TOTAL R$ {valorTotal}')
