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
compras = []

op = 0
while True:
    op = int(input('---- Bem-vindo ao PDV ----\n\nSelecione a opção desejada\n'
                   '1 - Registrar venda\n'
                   '2 - Registrar compra\n'
                   '3 - Resumo da loja\n'
                   '4 - Sair\n'
                   'Resposta: '))
    if op == 1:
        print('\n----- REGISTAR VENDA -----\n')
        print('COD | NOME | PREÇO | QTD')

        # LISTAR JOGOS
        for jogo in nomeJogos:
            print(f'{nomeJogos.index(jogo)}...{jogo}...'
                  f'R${precosVenda[nomeJogos.index(jogo)]:.2f}...'
                  f'{estoqueJogos[nomeJogos.index(jogo)]}')

        # SELECIONAR JOGO
        codigo = int(input('\nDigite o código do jogo: '))
        print(f'Nome: {nomeJogos[codigo]}')

        # INFORMAR QUANTIDADE
        while True:
            qtd = int(input('Digite a quantidade: '))
            if qtd <= estoqueJogos[codigo]:
                break
            else:
                print('\n[!] Quantidade informada é maior que estoque!')
                print(f'[!] Quantida em estoque: {estoqueJogos[codigo]}\n')

        # DEDUZ QUANTIDADE DO ESTOQUE
        estoqueJogos[codigo] -= qtd
        print(f'Quantidade atual no estoque: {estoqueJogos[codigo]}')

        # CALCULA VALOR TOTAL DA VENDA
        valorVenda = precosVenda[codigo] * qtd
        print(f'Valor total da venda: R${valorVenda:.2f}')
        vendas.append(valorVenda)

        # EXIBE RESUMO DA VENDA
        print('\n--- RESUMO DA VENDA ---')
        print(f'Nome do jogo: {nomeJogos[codigo]}\n'
              f'Quantidade: {qtd}\n'
              f'Valor total: R$ {valorVenda:.2f}\n'
              f'Vendas até o momento: {vendas}\n')

    elif op == 2:
        print('\n----- REGISTRAR COMPRA -----\n')
        print('COD | NOME | PREÇO | QTD')

        # LISTAR JOGOS
        for jogo in nomeJogos:
            print(f'{nomeJogos.index(jogo)}...{jogo}...'
                  f'R${precosVenda[nomeJogos.index(jogo)]:.2f}...'
                  f'{estoqueJogos[nomeJogos.index(jogo)]}')

        # SELECIONAR JOGO
        codigo = int(input('\nDigite o código do jogo: '))
        print(f'Nome: {nomeJogos[codigo]}')

        # INFORMAR QUANTIDADE
        qtd = int(input('Digite a quantidade: '))

        # ADICIONAR QUANTIDADE AO ESTOQUE
        estoqueJogos[codigo] += qtd
        print(f'Quantidade atual no estoque: {estoqueJogos[codigo]}')

        # CALCULA VALOR TOTAL DA COMPRA
        valorCompra = precosCusto[codigo] * qtd
        print(f'Valor total da compra: R${valorCompra:.2f}')
        compras.append(valorCompra)

        # EXIBE RESUMO DA COMPRA
        print('\n--- RESUMO DA COMPRA---')
        print(f'Nome do jogo: {nomeJogos[codigo]}\n'
              f'Quantidade: {qtd}\n'
              f'Valor total: R$ {valorCompra:.2f}\n'
              f'Compras até o momento: {compras}\n')

    elif op == 3:
        print('\n----- RESUMO DA LOJA -----\n')

        # EXIBIR ESTOQUE ATUAL
        print('--- Estoque atual --------')
        for jogo in nomeJogos:
            print(f'{jogo}: {estoqueJogos[nomeJogos.index(jogo)]} un.')

        # EXIBE TOTAL DE VENDAS
        print('--- Total de Vendas ------')
        totalVendas = 0
        for venda in vendas:
            print(f'Venda {vendas.index(venda)+1}: R$ {venda:.2f}')
            totalVendas += venda
        print(f'TOTAL: R${totalVendas:.2f}')

        # EXIBE TOTAL DE COMPRAS
        print('--- Total de Compras -----')
        totalCompras = 0
        for compra in compras:
            print(f'Compra {compras.index(compra) + 1}: R$ {compra:.2f}')
            totalCompras += compra
        print(f'TOTAL: R${totalCompras:.2f}')

        # CALCULAR LUCRO / PREJUÍZO
        print('--- Balanço --------------')
        print(f'Lucro / Prejuízo: R$ {totalVendas-totalCompras:.2f}\n')

    elif op == 4:
        print('CAIXA FECHADO!')
        break
    else:
        print('Opção inválida. Tente Novamente!')
