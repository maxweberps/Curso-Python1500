'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
e informe-o expresso no formato horas:minutos:segundos.
'''

duracao_seg = int(input())

h = duracao_seg // 3600
duracao_seg = duracao_seg % 3600

min = duracao_seg // 60
duracao_seg = duracao_seg % 60

seg = duracao_seg

print(f'{h}:{min}:{seg}')