'''
1) Crie uma classe chamada Personagem que irá receber como construtor o
nome completo, altura, peso e resistência (0-100) do personagem, além disso,
também crie um método que se chame poder que conterá todos os atributos de
instancia como privado não sendo possível alterá-los, sendo estes: magia,
persuasão, agilidade e forca, cada um avaliada de 0 a 100, por fim, retorne
apenas a soma de todos os pontos fornecidos. Crie 3 objetos personagens e
imprima o nome completo e quantidade de poder total do mais forte.
'''


class Personagem:
    def __init__(self, nome, altura, peso, resistencia):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.resistencia = resistencia

    def poder(self, magia, persuasao, agilidade, forca):
        self.__magia = magia
        self.__persuasao = persuasao
        self.__agilidade = agilidade
        self.__forca = forca
        return self.__magia + self.__persuasao + self.__agilidade + self.__forca

    def consultar_poder(self):
        return self.__magia + self.__persuasao + self.__agilidade + self.__forca


dict_personagens = {}

char01 = Personagem('Dulcius', 1.72, 73.5, 80)
dict_personagens[char01.nome] = char01.poder(99, 99, 0, 0)

char02 = Personagem('Zoroto', 1.80, 95, 90)
dict_personagens[char02.nome] = char02.poder(20, 99, 80, 99)

char03 = Personagem('Um Tiro de Justica', 1.72, 73.5, 80)
dict_personagens[char03.nome] = char03.poder(20, 50, 99, 0)

poder_max = 0
nome_max = ''
print('-- Lista de personagens e Poder --')
for nome, poder in dict_personagens.items():
    print(f'Nome: {nome}, Poder: {poder}')
    if poder > poder_max:
        nome_max = nome
        poder_max = poder
print(f'\nO personagem de maior pode é:\nNome: {nome_max}\nPoder: {poder_max}')
