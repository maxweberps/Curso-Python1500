frutas = ['pera', 'uva', 'maça']


def listar_frutas(frutas):
    yield frutas

# objeto do tipo generator
print(listar_frutas(frutas))
# converte em tupla
print(tuple(listar_frutas(frutas)))

