"""
1 - Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira,
potência).
Peça a operação desejada e depois os dois números ao usuário.
"""

opcao = int(input('Qual operação você deseja?\n'
                  '1 - Soma\n'
                  '2 - Substração\n'
                  '3 - Multiplicação\n'
                  '4 - Divisão\n'
                  '5 - Divisão (retornar inteiro)\n'
                  '6 - Exponenciação\n'
                  'Opção: '))

num1 = float(input('Valor 1: '))
num2 = float(input('Valor 2: '))

if opcao == 1:
    print(f'Resultado = {num1 + num2}')
elif opcao == 2:
    print(f'Resultado = {num1 - num2}')
elif opcao == 3:
    print(f'Resultado = {num1 * num2}')
elif opcao == 4:
    print(f'Resultado = {num1 / num2}')
elif opcao == 5:
    print(f'Resultado = {num1 // num2}')
elif opcao == 6:
    print(f'Resultado = {num1 ** num2}')
else:
    print('Opção inválida!')
