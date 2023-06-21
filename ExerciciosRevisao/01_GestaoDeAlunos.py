"""
Exercício: Gerenciamento de Alunos

# Crie um programa que permita o gerenciamento de alunos de uma escola. O programa deve
# ser capaz de realizar as seguintes operações:
# - Adicionar um aluno: o programa deve solicitar o nome e a nota do aluno, e adicioná-lo ao dicionário de alunos.
# - Remover um aluno: o programa deve solicitar o nome do aluno a ser removido, e removê-lo do dicionário de alunos.
# - Calcular a média das notas: o programa deve calcular a média das notas de todos os alunos.
# - Exibir a lista de alunos: o programa deve exibir a lista de todos os alunos e suas respectivas notas.
"""

alunos = {}


# FUNÇÃO ADICIONAR ALUNO
def adicionar_aluno():
    print('\n-- ADICIONAR ALUNO --')
    nome = input('Nome: ')
    nota = float(input('Nota: '))
    alunos[nome] = nota
    print('Aluno adicionado com sucesso!')


def remover_aluno():
    print('\n-- REMOÇÃO DE ALUNO --')
    nome = input('Nome: ')
    del alunos[nome]
    print(f'O aluno {nome} foi removido com sucesso!')


def calcular_media():
    print('\n-- MÉDIA DOS ALUNOS --')
    soma_notas = 0
    for i in alunos:
        soma_notas += alunos[i]
    print(f'A média das notas dos alunos é: {soma_notas/len(alunos):.1f}')


def exibir_lista():
    print('\n-- LISTA DE ALUNOS --')
    if len(alunos) == 0:
        print('Não há alunos no sistema!')
    else:
        for aluno, nota in alunos.items():
            print(f'{aluno}: {nota:.1f}')


# PRINCIPAL
while True:
    opcao = input('\nGERENCIAMENTO DE ALUNOS:\n'
                  '1 - Adicionar aluno\n'
                  '2 - Remover aluno\n'
                  '3 - Calcular média das notas\n'
                  '4 - Exibir lista de alunos\n'
                  '0 - Sair\n'
                  'R: ')

    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        remover_aluno()
    elif opcao == '3':
        calcular_media()
    elif opcao == '4':
        exibir_lista()
    elif opcao == '0':
        print('\nPrograma encerrado.')
        break
    else:
        print('Opção inválida!')
