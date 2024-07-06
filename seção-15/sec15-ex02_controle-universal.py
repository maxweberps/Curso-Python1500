'''
1 - Desenvolva o sistema de um controle universal para uma casa. O controle deve
ser a Classe-Mãe, que contém o método liga/desliga e é herdada por outras três
classes (equipamentos controlados): ar-condicionado, micro-ondas e televisão, que
controlam, respectivamente, temperatura, tempo e volume em métodos dentro das
classes. Além disso, os métodos construtores das Classes Filhas recebem a variável
controlada em seu valor atual, por exemplo 'temperaturaAtual'.
Obs.: Utilize também propriedades para realizar o acesso aos atributos.
'''


class Controle:
    ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado


class Arcondicionado(Controle):
    def __init__(self, temp_atual):
        self.__temp_atual = temp_atual

    def controle_temperatura(self, nova_temp):
        self.__temp_atual = nova_temp

    @property
    def temp_atual(self):
        return self.__temp_atual


class Microondas(Controle):
    def __init__(self, tempo_atual):
        self.__tempo_atual = tempo_atual

    def controle_tempo(self, novo_tempo):
        self.__tempo_atual = novo_tempo

    @property
    def tempo_atual(self):
        return self.__tempo_atual


ar1 = Arcondicionado(25)
print('Ar condicionado Ligado' if ar1.ligado else 'Ar condicionado Desligado', f', temperatura: {ar1.temp_atual}')
ar1.controle_temperatura(int(input('Nova temperatura: ')))
ar1.liga_desliga()
print('Ar condicionado Ligado' if ar1.ligado else 'Ar condicionado Desligado', f', nova temperatura: {ar1.temp_atual}\n')

micro1 = Microondas(10)
print('Microondas Ligado' if micro1.ligado else 'Microondas Desligado', f', tempo: {micro1.tempo_atual}')
micro1.controle_tempo(int(input('Novo tempo: ')))
micro1.liga_desliga()
print('Microondas Ligado' if micro1.ligado else 'Microondas Desligado', f', novo tempo: {micro1.tempo_atual}')