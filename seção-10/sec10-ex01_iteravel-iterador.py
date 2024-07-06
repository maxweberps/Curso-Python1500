def desmembra_iteravel(itereval):
    iterador = iter(itereval)
    while True:
        try:
            print(next(iterador))
        except StopIteration:
            print('Chegamos ao último elemento')
            break


desmembra_iteravel(['pera', 'uva', 'maçã', 'salada mista'])
