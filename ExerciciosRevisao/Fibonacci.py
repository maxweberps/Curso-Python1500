"""
Faça um programa que gere uma sequência Fibonacci. O usuario informa um número limite e o programa gera uma sequência
Fibonacci até esse limite, sem ultrapassá-lo.
"""

limite = int(input('Informa um limite para a sequencia Fibo: '))

a = 0
b = 1
seq = []

while a < limite:
    seq.append(a)
    a, b = b, a + b

print(seq)
