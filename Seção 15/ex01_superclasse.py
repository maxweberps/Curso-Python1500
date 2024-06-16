'''
1 - Crie uma SuperClasse chamada 'Pessoa' que recebe como atributos nome,
cpf e salário. Após isso, construa a Classe Filha: 'Funcionario', que possui o
método sem parâmetros chamado 'promocao', que apenas acrescenta 10% no
salário a algum funcionário. Por sua vez, a classe 'Funcionario' deve ser
Classe Mãe de outras duas classes: 'Gerente' e 'Estagiario', e ambos precisam
ter o atributo 'codigo' em seu método construtor. Além disso, o gerente precisa
do atributo 'numEstagiarios', representando a quantidade de funcionário que
ele é responsável. Ainda, na classe gerente deve haver um método que
possibilite a alteração do código dos estagiários, sendo que os estagiários não
têm acesso a troca de codigo. Instancie 3 estagiários e 1 gerente. Dê
promoção para os dois primeiros estagiários e para o gerente.
Obs.: Utilize também um método mágico para representar as classes
'Estagiário' e 'Gerente', e propriedades para acessar os atributos de 'Pessoa'.
'''


class Pessoa:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, aumento):
        self.__salario = aumento


class Funcionario(Pessoa):
    def promocao(self):
        self.salario *= 1.1


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, codigo, num_estagiarios, cod_estagiarios):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo
        self.__num_estagiarios = num_estagiarios
        self.__cod_estagiarios = cod_estagiarios

    def trocar_codigo(self, novo_cod):
        self.__cod_estagiarios = novo_cod

    def __repr__(self):
        return f'Sou o(a) {self.nome}, recebo R$ {round(self.salario)} e quero um café'


class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario, codigo):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo

    def __repr__(self):
        return (f'Sou o(a) estagiário(a) {self.nome}, recebo R$ {round(self.salario)} e tenho '
                f'que levar um café alí na administração.')


gerente01 = Gerente('Max Weber', "05591401341", 12000, "0235", 3, 'est1234')
estagiario01 = Estagiario('Marcos', "132645465", 1200, 'est1234')
estagiario02 = Estagiario('Matheus', "4365645465", 1200, 'est1234')
estagiario03 = Estagiario('Maicon', "164327465", 1200, 'est1234')

print(gerente01.__repr__())
print(estagiario01.__repr__())
print(estagiario02.__repr__())
print(estagiario03.__repr__())

print('\n')

estagiario01.promocao()
gerente01.promocao()

print(gerente01.__repr__())
print(estagiario01.__repr__())