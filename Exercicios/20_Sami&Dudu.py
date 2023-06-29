"""
1) Sami e Dudu irão fazer uma competição de quem visita mais Estados no Brasil
em um período de 6 meses, até então Dudu já visitou o Espírito Santo e São
Paulo, enquanto Sami visitou Rio de Janeiro e Bahia. Crie dois conjuntos
diferentes para simbolizar os estados que cada um foi. Após 6 meses Dudu
visitou Bahia, Acre, Santa Catarina e Sergipe, enquanto Sami visitou Bahia,
Minas Gerais, Amazonas e Paraná, atualize cada um dos conjuntos com os
novos Estados. Responda:
- Quais Estados Dudu visitou que Sami não foi?
- Quais Estados ambos foram?
- Sendo 27 Estados no Brasil todo, qual porcentagem o vencedor visitou?
"""

uf_dudu = {'Espírito Santo', 'São Paulo'}
uf_sami = {'Rio de Janeiro', 'Bahia'}

print(f'Estados que o Dudu visitou: {uf_dudu}')
print(f'Estados que a Sami visitou: {uf_sami}')

print('\n6 meses depois....\n')

uf_dudu.add('Bahia')
uf_dudu.add('Acre')
uf_dudu.add('Santa Catarina')
uf_dudu.add('Sergipe')

uf_sami.add('Bahia')
uf_sami.add('Minas Gerais')
uf_sami.add('Amazonas')
uf_sami.add('Paraná')
uf_sami.add('Ceará')
uf_sami.add('Paraiba')
uf_sami.add('Piaui')

print(f'Estados que o Dudu visitou: {uf_dudu}.'
      f'\nTOTAL: {len(uf_dudu)} estados!')
print(f'Estados que a Sami visitou: {uf_sami}.'
      f'\nTOTAL: {len(uf_sami)} estados!')

print('\n---- ESTATÍSTICAS ----')
print(f'Estados que o Dudu visitou e a Sami não: {uf_dudu.difference(uf_sami)}'
      f'\nTOTAL: {len(uf_dudu.difference(uf_sami))}')
print(f'Estados que ambos visitaram: {uf_dudu.intersection(uf_sami)}'
      f'\nTOTAL: {len(uf_dudu.intersection(uf_sami))}')

print('\n---- RESULTADO ----')
if len(uf_dudu) > len(uf_sami):
    print(f'Vencedor: Dudu'
          f'\nCom total de {len(uf_dudu)} estados visitados!'
          f'\nDiferença de {len(uf_dudu) - len(uf_sami)} estado(s) a mais!'
          f'\nAté então, visitou {(len(uf_dudu) / 27) * 100:.0f}% dos estados brasileiros')
else:
    print(f'Vencedor: Sami'
          f'\nCom total de {len(uf_sami)} estados!'
          f'\nDiferença de {len(uf_sami) - len(uf_dudu)} estado(s) a mais!'
          f'\nAté então, visitou {(len(uf_sami) / 27) * 100:.0f}% dos estados brasileiros')
