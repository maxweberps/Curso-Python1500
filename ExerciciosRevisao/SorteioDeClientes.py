import random

nomes = []
telefones = []

print('---- LOJA DE DOCES ----')
print('-> Lançar vendas')
while True:
    nome = input('Nome do cliente: ')
    if nome == 'fim':
        break
    else:
        nomes.append(nome)
        telefones.append(input('Telefone do cliente: '))

indice_sorteado = random.randint(0, len(nomes) - 1)

print(f'\n---- Sorteio ----\n'
      f'O cliente sorteado é: {nomes[indice_sorteado]}\n'
      f'Telefone do cliente: {telefones[indice_sorteado]}\n'
      f'Parabéns!')
