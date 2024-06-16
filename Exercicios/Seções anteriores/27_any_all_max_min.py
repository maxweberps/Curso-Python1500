'''
1 - Criar uma lista e uma tupla com diversos valores, separar os valores máximos e
mínimos de cada uma em um conjunto. Por fim, verificar se os 4 valores separados
são verdadeiros ou falsos utilizando o any e o all.
'''

num_a = [0, 5, 12, 16, 45, 6]
num_b = (12, 24, 19, 4, 28)
conjunto = {max(num_a), min(num_a), max(num_b), min(num_b)}
print(conjunto)
print(any(conjunto))  # retorna true se pelo menos 1 valor do conjunto for true
print(all(conjunto))  # retorna true se todos os valores do conjunto o for true

palavra = 'roma'
# palavra_invertida = (list(reversed(palavra)))
nova_palavra = ''
for letra in reversed(palavra):
    nova_palavra += letra

print(nova_palavra)

print(palavra[::-1])
