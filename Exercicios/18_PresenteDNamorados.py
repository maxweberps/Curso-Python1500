"""
Chegou o famoso dia dos namorados, Mateus deixou para decidir o presente em cima da hora.
Ele resolveu comprar um tipo de flor, um presente e escolher um lugar para saírem, ele anotou todas as opções abaixo:
           Flores
     Tipo	       Preço
Rosas Vermelhas	  145,00
Girassóis	      125,00
Margaridas	      120,00
Flores do campo	  140,00

          Presente
     Tipo	       Preço
Urso de Pelúcia	   55,00
Caixa de Bombom	   60,00
Colar	           75,00
Roupas	           40,00

           Lugar
      Tipo	         Preço
Praia	             70,00
Sair para jantar	150,00
Parque de diversões	120,00
Hotel	            180,00

- Crie um programa que descubra qual a combinação mais cara, em seguida mais barata e a média opção.
Imprima a combinação em cada caso.
- Use um dicionário para cada item (flor, lugar e presente).
"""

# Declaração dos dicionários
flores = {'Rosas Vermelhas': 145, 'Girassóis': 125, 'Margarida': 120, 'Flores do campo': 140}
presentes = {'Urso de pelucia': 55, 'Caixa de bombom': 60, 'Colar': 75, 'Roupas': 40}
lugares = {'Praia': 70, 'Sair para jantar': 150, 'Parque de Diversao': 120, 'Hotel': 180}

# KIT MAIS CARO
preco_maior = 0
preco_atual = 0
flor_mais_cara = None
presente_mais_caro = None
lugar_mais_caro = None

# CALCULAR KIT MAIS CARO
for flor, preco1 in flores.items():
    for presente, preco2 in presentes.items():
        for lugar, preco3 in lugares.items():
            preco_atual = preco1 + preco2 + preco3
            if preco_atual > preco_maior:
                preco_maior = preco_atual
                flor_mais_cara = flor
                presente_mais_caro = presente
                lugar_mais_caro = lugar

# MONTAR DICIONÁRIO COM OS ITENS MAIS CAROS
kit_mais_caro = {flor_mais_cara: flores[flor_mais_cara],
                 presente_mais_caro: presentes[presente_mais_caro],
                 lugar_mais_caro: lugares[lugar_mais_caro]}

# EXIBIR KIT MAIS CARO
print(f'\n--- KIT MAIS CARO ----\n'
      f'{kit_mais_caro}\n'
      f'Total: R$ {preco_maior}')

# KIT MAIS BARATO
preco_menor = 0
preco_atual = 0
flor_mais_barata = None
presente_mais_barato = None
lugar_mais_barato = None

# CALCULAR KIT MAIS BARATO
aux = 0
for flor, preco1 in flores.items():
    for presente, preco2 in presentes.items():
        for lugar, preco3 in lugares.items():
            if aux == 0:
                preco_menor = preco1 + preco2 + preco3
                aux += 1
            else:
                preco_atual = preco1 + preco2 + preco3
                if preco_atual < preco_menor:
                    preco_menor = preco_atual
                    flor_mais_barata = flor
                    presente_mais_barato = presente
                    lugar_mais_barato = lugar

# MONTAR DICIONÁRIO COM OS ITENS MAIS BARATOS
print(flor_mais_barata)
kit_mais_barato = {flor_mais_barata: flores[flor_mais_barata],
                   presente_mais_barato: presentes[presente_mais_barato],
                   lugar_mais_barato: lugares[lugar_mais_barato]}

# EXIBIR KIT MAIS BARATO
print(f'\n--- KIT MAIS BARATO ----\n'
      f'{kit_mais_barato}\n'
      f'Total: R$ {preco_menor}')

# KIT CUSTO MÉDIO

kit_custo_medio = {}
custo_kits = []
preco_total = 0
for flor, preco1 in flores.items():
    for presente, preco2 in presentes.items():
        for lugar, preco3 in lugares.items():
            preco_total = preco1 + preco2 + preco3
            custo_kits.append(preco_total)

print(f'\n--- KIT CUSTO MÉDIO ----\n')
custo_kits.sort()
print(f'O preco do kit com custo médio é R$ {custo_kits[(len(custo_kits) // 2)]}')

preco_total = 0
aux = 1
for flor, preco1 in flores.items():
    for presente, preco2 in presentes.items():
        for lugar, preco3 in lugares.items():
            preco_total = preco1 + preco2 + preco3
            if preco_total == custo_kits[(len(custo_kits) // 2)]:
                kit_custo_medio[aux] = (flor,preco1,presente,preco2,lugar,preco3)
                aux += 1

print(kit_custo_medio)