'''
Aplique o procedimento Try/Except/Else/Finally no seguinte código que realiza um cadastro de formulário
para uma pessoa realizar uma viagem.
'''

opcoes_viagem = {1: 'EUA', 2: 'França', 3: 'Japão', 4: 'Brasil'}
try:
    nome = input('Seu nome: ')
    teste = int(nome)
except ValueError:
    try:
        idade = int(input('Sua idade: '))
    except ValueError:
        print('A idade precisa ser um número inteiro.')
    else:
        cont = 0
        print('Opções de destino: ')
        for i in opcoes_viagem:
            cont += 1
            print(f'{i} - {opcoes_viagem[i]}')
        try:
            lugar = int(input('Digite o número referente ao destino desejado: '))
        except ValueError:
            print('A resposta deve ser um número inteiro.')
        else:
            try:
                pais = opcoes_viagem[lugar]
            except KeyError:
                print('Opção de destino inválida.')
            else:
                print(f'O pais escolhi foi {pais}')
            finally:
                print('Cadastro finalizado.')
else:
    print('Digite um nome válido.')
