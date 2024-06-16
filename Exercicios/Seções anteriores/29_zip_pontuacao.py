'''
1 - Está acontecendo uma gincana na Escola e você foi escolhido(a) para
realizar o controle da pontuação! Para isso, crie 4 listas (A primeira com nome
das pessoas que participam da gincana. As outras 3 (cada uma representando
uma prova) armazenam valores de 0 a 100, ou seja, as notas que cada
participante obteve. Por fim, utilize zip() para retornar um dicionário
com o nome de cada aluno como chave e o somatório de suas notas em cada
prova como valor. Após isso, imprima o participante vencedor.
'''

nomes = ['maria', 'joao', 'janny', 'raquel']
prova_corrida = [2, 5, 4, 2]
prova_escalada = [4, 8, 1, 2]
prova_burpee = [5, 10, 8, 5]

lista_notas = []
tabela = zip(prova_corrida, prova_escalada, prova_burpee)

for notas in tabela:
    lista_notas.append(sum(notas))

dicio_final = dict(zip(nomes, lista_notas))
print(dicio_final)

pts_maior = 0
vencedor = ''
for nome, pontos in dicio_final.items():
    if pontos > pts_maior:
        vencedor = nome
        pts_maior = pontos

print(f'O vencedor é: {vencedor}')
print(f'Com um total de {pts_maior} pontos')