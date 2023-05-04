"""
1) Faça um programa que calcule o maior palíndromo resultado do produto de
dois números de 3 dígitos. - Palíndromo são números que lendo da esquerda para a direita resulta no
mesmo número caso leia da direita para esquerda. Ex: 52625
- Ex: O maior palíndromo resultado do produto de dois números é 91*99 = 9009
"""

n1 = 999
maiorPali = 0

while n1 != 0:
    n2 = n1
    while n2 != 0:
        res = str(n1 * n2)
        invertidoStr = res[::-1]
        if res == invertidoStr:  # Testa Pali
            invertidoInt = int(invertidoStr)
            if maiorPali < invertidoInt:
                maiorPali = invertidoInt
            else:
                n2 -= 1
        else:
            n2 -= 1
    n1 -= 1

print(maiorPali)
