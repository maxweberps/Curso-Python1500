# Exercício: Cálculo de Quadrados

# Crie um programa que solicite ao usuário um número inteiro N e gere um dicionário
# usando dictionary comprehension. As chaves do dicionário devem ser os números de 1 a N
# e os valores devem ser o quadrado de cada número.

# Exemplo:
# Entrada: 5
# Saída: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = int(input('Digite um número: '))
quadrado = {num: num ** 2 for num in range(1, n + 1)}
print(quadrado)
