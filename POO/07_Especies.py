'''
1 - Crie duas classes chamadas 'Homem' e 'Urso', que recebem apenas nome
como parâmetro. Estas classes devem herdar de outras duas chamadas
'Carnivoros' e 'Herbivoros', que possuem dois métodos cada ('caçar_animal' e
'comer_carne' para 'Carnivoros', 'procurar_arvore' e 'comer_folhas' para
'Herbivoros') e herdam de uma Superclasse chamada 'Animal', na qual possui
os métodos 'andar' e 'correr'. Por fim, instancie dois objetos, da classe 'Homem'
e da classe 'Urso', e execute todos os métodos.
Obs.: Crie um método para as classes 'Homem' e 'Urso' representando uma
ação característica de cada, por exemplo ler um livro para o homem e hibernar
para o urso.
'''


class Animal:

    def andar(self, passos):
        print(f'Andou {passos} passos....')

    def correr(self, distancia):
        print(f'Correu {distancia} metros')


class Carnivoros(Animal):
    def cacar_animal(self):
        print('Caçando um animal....')

    def comer_carne(self):
        print('Comendo uma caininha assada!')


class Herbivoros(Animal):
    def procurar_arvore(self):
        print('Procurando uma plantinha..')

    def comer_folhas(self):
        print('Comendo um alface...')


class Homem(Carnivoros, Herbivoros):
    def __init__(self, nome):
        self.nome = nome

    def ler_livro(self, titulo):
        print(f'O(a) chamado {self.nome} irá ler o livro {titulo}')


class Urso(Carnivoros, Herbivoros):
    def __init__(self, nome):
        self.nome = nome

    def hibernar(self, tempo_meses):
        print(f'O urso {self.nome} irá hibernar por {tempo_meses} meses...')


# instanciando objetos
homem01 = Homem('Max')
urso01 = Urso('Poo')

# metodos
homem01.ler_livro('O pequeno princepe')
homem01.andar(200)
homem01.correr(100)
homem01.cacar_animal()

urso01.hibernar(6)
urso01.correr(500)
urso01.procurar_arvore()
urso01.comer_folhas()
