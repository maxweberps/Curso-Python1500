# 1 - Realizar a média das notas de 4 alunos
notaPedro = float(input('Nota do Pedro: '))
notaJunior = float(input('Nota do Junior: '))
notaMaria = float(input('Nota da Maria: '))
notaAna = float(input('Nota da Ana: '))

media = (notaPedro + notaJunior + notaMaria + notaAna) / 4
print(f'A média das notas dos alunos é {media}')

# 2 - Converter uma temperatura de graus °C para ºF e para K.
# Dados: ºF = ºC * 1.8 + 32, K = ºC + 273.15

C = float(input('Temperatura em Celsius: '))
print(f'Convetido para Fa: {C*1.8+32}')
print(f'Temperatura em K: {C+273.15}')