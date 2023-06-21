# Exercício: Contagem de Caracteres

# Crie um programa que receba uma string do usuário e gere um dicionário usando dictionary
# comprehension. As chaves do dicionário devem ser os caracteres presentes na string
# (desconsiderando os espaços em branco) e os valores devem ser a contagem de ocorrências
# de cada caractere na string.

# Exemplo:
# Entrada: "Hello, world!"
# Saída: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

frase = input('Digite um frase: ')
contagem = {c: frase.count(c) for c in frase if c != " "}
print(contagem)

print(
    f'O caractere que mais se repete é "{max(contagem, key=contagem.get)}",'
    f' se repete {contagem[max(contagem, key=contagem.get)]} vezes')
