"""
Escreva uma função que recebe uma lista como argumento e retorna
uma nova lista contendo apenas os elementos únicos da lista original.
"""


def elementos_unicos(lista):
    elementos_unicos = []
    for elemento in lista:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
    return elementos_unicos


lista = [5, 5, 2, 3, 4, "Amor", "Amor", "Vento", "Terra", "Ar", "Ar", "Fogo"]
print(lista)
lista_nova = elementos_unicos(lista)
print(lista_nova)
