def consulta_palindromo(palavra1, palavra2):
    print(palavra1)
    print(palavra2)
    if palavra1 == palavra2:
        print('É pali')
    else:
        print('Não é pali')


palavra = input('Digite uma palavra: ')

# metodo 1
print('medoto 1')
nova_palavra = palavra[::-1]
consulta_palindromo(palavra, nova_palavra)

# metodo 2
print('\nmedoto 2')
nova_palavra = ''
for letra in reversed(palavra):
    nova_palavra += letra
consulta_palindromo(palavra, nova_palavra)

# metodo 3
print('\nmedoto 3')
nova_palavra = ''
for i in range(len(palavra) - 1, -1, -1):
    nova_palavra += palavra[i]
print(f'nova_palavra: {nova_palavra}')
consulta_palindromo(palavra, nova_palavra)
