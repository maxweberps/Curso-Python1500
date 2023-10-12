palavra = input('Digite uma palavra: ')

nova_palavra = palavra[::-1]

print(palavra)
print(nova_palavra)

if nova_palavra == palavra:
    print('é um palindromo')
else:
    print('não é palindromo')