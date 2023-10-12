limite = int(input('Deseja testar os numeros primos até quanto? '))
primos = []

for num in range(1, limite + 1):
    qtd_div = 0
    for i in range(1, num + 1):
        if num % i == 0:
            qtd_div += 1
    if qtd_div == 2:
        primos.append(num)

print(primos)
