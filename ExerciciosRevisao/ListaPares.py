"""
Escreva uma função que recebe uma lista e retorna uma nova lista contendo apenas os números pares da lista origina
"""
def select_pares(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
    return pares


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
print(f'Numeros pares: {select_pares(lista)}')
