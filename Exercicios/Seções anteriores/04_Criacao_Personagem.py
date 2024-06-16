"""
2) Criação de personagem de mundo de ficção, apresentando opções de acordo
com os tipos das variáveis:
- Cor de Cabelo (string)
- Cor de pele (string)
- Classe: Guerreiro, Mago, Arqueiro (string)
- Idade (int)
- Altura (float)
- Habilidade Específica (string)
Imprima para o usuário o personagem completo.
"""
print('------ Crie seu personagem --------')
nome = input('Nome do personagem: ')
cor_cabelo = input('Cor do cabelo: ')
cor_pele = input('Cor da pele: ')
classe = input('Escolha a classe do seu personagem: \n'
               '1 - Guerreiro\n'
               '2 - Mago\n'
               '3 - Arqueiro\n'
               'Opção: ')
idade = int(input('Idade: '))
altura = float(input('Altura: '))
habilid = input('Habilidade: ')

## Exibir personagem
print(f'\nSeu personagem: \nNome: {nome}\n'
      f'Cor do cabelo: {cor_cabelo}\n'
      f'Cor da pele: {cor_pele}\n'
      f'Classe: {classe}\n'
      f'Idade: {idade} anos\n'
      f'Altura: {altura} metros\n'
      f'Habilidade: {habilid}')
