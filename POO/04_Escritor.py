'''
1 - Um escritor de livros pretende escrever e lançar edições para atingir a
quantia de 1 milhão de reais. Simplesmente por este motivo, crie uma classe
que receberá em seu método construtor o nome do livro e o número de
páginas. Além disso, também deve ser criado um atributo no construtor para a
edição do livro, que será atualizado em uma unidade a cada livro que for
publicado. Por fim, utilize randint() para gerar um valor entre 0 e 500 mil,
representando a arrecadação das vendas, o último atributo do construtor.
Crie o método mágico __repr__ para representar o nome do livro e a edição.
Ainda, utilize __len__ para determinar o número de páginas de cada livro. Por
fim, verifique se o valor total de arrecadações atingiu 1 milhão de reais.
'''
import random


class Livro:
    edicao = 0

    def __init__(self, nome, num_pags):
        self.nome = nome
        self.num_pags = num_pags
        self.edicao += 1
        self.arrec = random.randint(0, 500000)

    def __len__(self):
        return self.num_pags

    def __repr__(self):
        return (f'Título: {self.nome}\n'
                f'Edição: {self.edicao}\n'
                f'Páginas: {self.num_pags}\n'
                f'Valor arrecadado: R$ {self.arrec:.2f}')


livro01 = Livro('HP', 551)
print(livro01, '\n')

livro02 = Livro('HP', 551)
print(livro02, '\n')

livro03 = Livro('HP', 551)
print(livro03, '\n')

total_arrecadado = livro01.arrec + livro02.arrec + livro03.arrec
print(f'\nTotal arrecadado: R$ {total_arrecadado:.2f}')
if total_arrecadado > 1000000:
    print(f'\nParabéns, conseguiu.')
else:
    print('\nInfelizmente ainda não.. continue a nadar......')
