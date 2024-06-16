'''
1 - Criar duas listas de mesmo tamanho preenchidas com números inteiros e
retornar outra lista com a soma das duas listas sendo uma delas invertida
(indice 0 com indice 9 para uma lista de tamanho 10, por exemplo), utilizando
lambda e comprehensions para iterar em ambas.
'''

lista1 = [10, 20, 40, 52, 85, 45, 60, 85, 100, 1]
lista2 = [120, 201, 402, 528, 854, 452, 603, 856, 102, 2]
lista3 = []

lista2.reverse()  # inverte os valores da lista2
soma = lambda lista1, lista2: [lista1[num] + lista2[num] for num in range(0, 10)]

lista3.append(soma(lista1, lista2))
print(lista3)
