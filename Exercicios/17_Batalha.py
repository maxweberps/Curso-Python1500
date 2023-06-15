"""
1) Faça um programa que contabiliza time de heróis e vilões da seguinte forma:
- Crie um dicionário chamado herói com chave sendo o nome do personagem e
o elemento o nível de poder do personagem entre 1 a 100. Ex: herói =
{‘Flash’:85}.
- Crie outro dicionário que serão as armas que podem ser usadas pelo herói,
sendo a chave o nome da arma e o elemento o nível de poder de 0 a 100. Ex:
arma = {‘Escudo do Capitão América’:60}
- Crie um último dicionário representado os vilões sendo a chave o nome e o
elemento o nível de poder de 0 a 200. Ex: vilao={‘Thanos’:175}
Após isso o usuário poderá escolher um herói, uma arma soma os pontos de
poder e escolher um vilao para lutar, apresente quem foi o vencedor, caso for o
herói imprima a arma usada. Caso resulte em empate informe na saída.
Observação: Pode definir qualquer herói,vilao e arma que quiser.
"""

herois = {"Dulcius": 99, "Riku": 86, "A Formula do Amor": 98, "Kafreudo": 73}
armas = {"Machado Mjolnir": 88, "Cajado da Magia Oculta": 100, "Injetor Álgido": 99}
inimigos = {
    'General Tartaruga': 180,
    'Thanatos': 195,
    'Ifrit': 174
}

print('Escolha um personagem: ')
for i, heroi in enumerate(herois):
    print(f'{i + 1}. {heroi}')
heroiEscolhido = input('R: ')

print('\nEscolha uma arma: ')
for i, arma in enumerate(armas):
    print(f'{i + 1}. {arma}')
armaEscolhida = input('R: ')

poderHeroi = herois[heroiEscolhido] + armas[armaEscolhida]

print('\nEscolha um  adversário: ')
for i, mvp in enumerate(inimigos):
    print(f'{i + 1}. {mvp}')
mvpEscolhido = input('R: ')

if poderHeroi > inimigos[mvpEscolhido]:
    print(f'\nParanbéns, {heroiEscolhido}!! '
          f'Você ganhou a batalha contra {mvpEscolhido}, '
          f'usando a arma {armaEscolhida} '
          f'e um total de poder de {poderHeroi}!!')
elif poderHeroi < inimigos[mvpEscolhido]:
    print(f'\nVocê perdeu, {heroiEscolhido}.. '
          f'Infelizmente, seu poder de batalha de {poderHeroi} '
          f'não foi suficiente contra o monstro {mvpEscolhido}. Continue treinando.')
else:
    print(f'\nPorrã, {heroiEscolhido}. Deu empate.. Seu poder de batalha de {poderHeroi} '
          f'é o mesmo que o do monstro {mvpEscolhido}')
