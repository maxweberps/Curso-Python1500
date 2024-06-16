"""
Para todos os números de 1 a 99, use Dict Comprehension para encontrar o dígito único mais alto em que qualquer
um dos números é divisível.
Ex: 64 tem o maior divisor de digito único de 8, pois 9 não é divisor de 64.
"""

resultado = {num: max([divisor for divisor in range(1, 10) if num % divisor == 0]) for num in range(1, 100)}
print(resultado)
