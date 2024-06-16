'''
2 - Realizar o cálculo do IMC através de uma função utilizando map com os
dados fornecidos abaixo sobre peso e altura, e salvar os resultados em outra
lista. Após isso, aplicar o filter para separar pessoas obesas (IMC > 25).
Dados:
índice 0 das tuplas: peso (kg)
índice 1 das tuplas: altura (m)
listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (54, 1.56), (69, 1.76), (112,
1.63), (98, 1.59)]
'''


def calcular_imc(amostra):
    return round(amostra[0] / (amostra[1]**2))


listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (54, 1.56),
                 (69, 1.76), (112, 1.63), (98, 1.59)]

resultado_imcs = map(calcular_imc, listaAmostras)
lista_obesos = filter(lambda imc: imc > 25, resultado_imcs)
print(f'IMCs acima do peso: {list(lista_obesos)}')
