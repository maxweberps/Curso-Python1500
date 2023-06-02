"""
1 - Criar um sistema de comando de uma loja de jogos. O programa deve
conter pelo menos 6 listas: uma indicando quais jogos estão disponíveis para
venda, uma para mostrar o preço de cada jogo, uma para mostrar a quantidade
de jogos disponíveis na loja para venda, uma informando o preço de fábrica
dos jogos para aumentar o estoque, uma para registrar as vendas e uma para
registrar as compras de estoque. Todas as informações de um jogo devem
estar no mesmo índice nas listas. Criar um menu interativo com as seguintes
opções para o usuário: Registrar venda, Compra de estoque, Resumo da loja,
Sair. Ao sair indicar que o caixa está fechado. O usuário deve controlar o
sistema da loja, registrando as vendas e as compras de estoque, sem esquecer
de alterar os valores da lista de quantidade.
"""

nomeJogos = ['Kingdom Hearts', 'GTA V', 'Hogwarts Legacy', 'Resident Evil 7']  # Jogos disponíveis para venda
precosVenda = [29.90, 149.99, 299.90, 170.00]  # Preços dos jogos
precosCusto = [9.90, 105.90, 130.00, 120.00]  # Preços de custo
estoqueJogos = [6, 10, 20, 13]  # Quantidade de jogos disponívies
vendas = []
comprasReporEstoque = []

op = 0
while True:
    op = int(input('---- Bem-vindo ao PDV ----\n\nSelecione a opção desejada\n'
                   '1 - Registrar venda\n'
                   '2 - Pedido de compra\n'
                   '3 - Resumo da loja\n'
                   '4 - Sair\n'
                   'Resposta: '))
    if op == 1:
        print('\n----- REGISTAR VENDA -----\n')
        print('COD | NOME | PREÇO | QTD')
        indice = 0
        while indice < len(nomeJogos):
            print(f'{indice}...{nomeJogos[indice]}...R$ {precosVenda[indice]:.2f}...{estoqueJogos[indice]}')
            indice += 1
        codigo = int(input('\nDigite o código do jogo: '))
        print(f'Nome: {nomeJogos[codigo]}')
        qtd = int(input('Digite a quantidade: '))
        valorVenda = precosVenda[codigo] * qtd
        print(f'Valor total da venda: R${valorVenda:.2f}')
        vendas.append(valorVenda)
        # falta conferir se a quantidade pedida é menor ou igual que o estoque
        # falta descontar o quantidade solicitada do estoque

        print('\n--- RESUMO DA VENDA---')
        print(f'Nome do jogo: {nomeJogos[codigo]}\n'
              f'Quantidade: {qtd}\n'
              f'Valor total: R$ {valorVenda:.2f}\n'
              f'Vendas até o momento: {vendas}\n')

    elif op == 2:
        print('Opção 2')
    elif op == 3:
        print('Opção 3')
    elif op == 4:
        print('Opção 4')
        break
    else:
        print('Opção inválida. Tente Novamente!')
