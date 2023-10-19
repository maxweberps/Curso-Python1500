'''
1 - Crie 3 listas: uma com o nome de 3 companhias aéreas, e as outras duas
representando o número de passageiros por companhia em dois voos: voo1 e
voo2. Utilize zip(), lambda e map() para obter o valor máximo de passageiros
por companhia nos dois voos e associar estes valores com o nome das
companhias, formando uma lista de tuplas. Por fim, utilizar filter() e lambda
para determinar a classificação da companhia, conforme indicado nos dados
abaixo.
Dados:
0 < Passageiros <= 100: 1 estrela.
100 < Passageiros <= 200: 2 estrelas.
200 < Passageiros <= 300: 3 estrelas.
'''

companhias = ['GOL', 'LATAM', 'AZUL']
voo1 = [115, 95, 110]
voo2 = [195, 80, 225]

# une os voos por companhia
voos1e2 = list(zip(voo1, voo2))
print(voos1e2)

# retorna a qtd máxima de passageiros que cada companhia levou
max_pass = map(lambda voos: max(voos), voos1e2)
companhias_max_pass = list(zip(companhias, max_pass))
print(companhias_max_pass)

# classifica as companhias
uma_estrela = list(filter(lambda max_voo: max_voo[1] <= 100, companhias_max_pass))  # 0 < Passageiros <= 100: 1 estrela.
duas_estrela = list(filter(lambda max_voo: 100 < max_voo[1] <= 200, companhias_max_pass))  # 100 n < Passageiros <= 200: 2 estrelas.
tres_estrela = list(filter(lambda max_voo: 200 < max_voo[1] <= 300, companhias_max_pass))  # 200 < Passageiros <= 300: 3 estrelas.

print(f'Companhia uma estrela: {uma_estrela}')
print(f'Companhia duas estrelas: {duas_estrela}')
print(f'Companhia tres estrelas: {tres_estrela}')
