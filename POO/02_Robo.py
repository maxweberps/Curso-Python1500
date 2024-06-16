'''
1) Crie uma classe Robo para controlar o objeto R2D2 com os seguintes
métodos:
- Construtor: Recebe como atributo a bateria que varia entre 0 e 100 e cria um
atributo de instancia chamado estado que apresenta se o robô está ligado ou
desligado.
- liga_desliga: Quando esse método é chamado o robô passa a ser ligado caso
esteja desligado e vice-versa.
- movimento: Recebe como atributo uma string, que representa qual o lado que
o robô irá andar e decresce o atributo bateria em 10 para cada execução desse
método.
- controle_energia: Imprime os atributos estado e bateria atualizados do Robo.
Crie uma interface de menu para o Usuário decidir o que irá fazer com o Robo,
ou seja, qual método irá acessar. Faça tratamento de erros com
Try/Except/Else/Finally. Trate também as condições especiais como bateria
zerada o que irá acontecer com o seu R2D2? Dentre outros, fica a cargo de
cada programador.
'''


class Robo:

    def __init__(self, bateria, estado):
        self.bateria = bateria
        self.estado = estado

    def liga_desliga(self):
        self.estado = not self.estado

    def movimento(self, lado):
        print(f'1 passo para {lado}')
        self.bateria -= 10
        print(f'Bateria: {self.bateria}')

    def controle_energia(self):
        print(f'Bateria {self.bateria}')
        print('Robo ligado' if self.estado else 'Robo desligado')


robo01 = Robo(100, True)
while True:
    print('\n-- Menu Robô --')
    op = input('1 - Ligar/Desligar\n'
               '2 - Consultar energia\n'
               '3 - Movimentar\n'
               '4 - Sair\n'
               'R: ')
    if op == '4':
        print('Fim')
        break
    elif op == '1':
        robo01.liga_desliga()
    elif op == '2':
        robo01.controle_energia()
    elif op == '3':
        robo01.movimento(input('Movimentar para qual lado? '))
