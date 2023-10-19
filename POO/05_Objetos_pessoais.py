class Obejetos:

    def __init__(self, nome_dono, videogame, senha_celular, dinheiro, camisa, livro):
        self.__videogame = videogame
        self.__senha_celular = senha_celular
        self.__dinheiro = dinheiro
        self.nome_dono = nome_dono
        self.camisa = camisa
        self.livro = livro

    @property
    def videogame(self):
        return f'O objeto {self.__videogame} é privado'

    @property
    def senha_celular(self):
        return f'A minha senha {self.__senha_celular} é privada'

    @property
    def dinheiro(self):
        return f'Essa valor de R$ {self.__dinheiro:.2f} é privado'

    @dinheiro.setter
    def dinheiro(self, valor):
        self.__dinheiro = valor

    def __repr__(self):
        return (f'O objeto {self.__videogame} de {self.nome_dono} é privado.\n'
                f'A senha {self.__senha_celular} de {self.nome_dono} é privada\n'
                f'Esse valor de R$ {self.__dinheiro:.2f} é privado\n')


joao = Obejetos('João', 'PS5', 'joao123', 500, 'Camisa da Polo', 'Harry Potter')
maria = Obejetos('Maria', 'XBOX', 'maria123', 1300, 'Vestido vermelho', 'O pequeno principe')

# get's
print(joao.videogame)
print(joao.senha_celular)
print(joao.dinheiro, '\n')

print(maria.videogame)
print(maria.senha_celular)
print(maria.dinheiro)
print('\nEdiatando dinheiro...\n')

# set's
joao.dinheiro = 14000
maria.dinheiro = 11000

# consultando por meio de metodo magico __repr__
print(maria)
print(joao)

