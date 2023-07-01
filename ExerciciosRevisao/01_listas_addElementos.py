"""
Escreva um programa que cria uma lista vazia e permite ao usuário
adicionar elementos a essa lista até que ele digite "sair".
"""

lista = []
while True:
    elemento = input('Digite o elemento: ')
    if elemento == 'sair':
        print('Encerrado!')
        break
    else:
        lista.append(elemento)
        print('Elemento adicionado!')
