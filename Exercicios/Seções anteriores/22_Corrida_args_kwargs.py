'''
1 - Faça o sistema de uma corrida entre MerCúrio, Papa-Léguas, SoNic, FlaSh,
LiGeirinho e Super Homem (MC, PL, SN, FS, LG, SH). Crie uma função que
receba os 6 corredores em ordem do vencedor até o último (pedir ao usuário),
sendo os três primeiros em variáveis obrigatórias e os três últimos em kwargs,
com as chaves sendo as posições na corrida. Pedir ao usuário se houve
trapaça:
- se não houve: apresentar a classificação final.
- se houve: pedir ao usuário quem trapaceou e quem foi prejudicado. Depois,
trocá-los de posições. Por fim, apresentar a classificação final.
'''


def classif_parcial(primeiro, segundo, terceiro, **outros):
    op = input('Houve trapaça? s/n: ')
    quarto = ''
    quinto = ''
    ultimo = ''
    if op == 'n':
        for posicao, corredor in outros.items():
            if posicao == '4':
                quarto = corredor
            elif posicao == '5':
                quinto = corredor
            elif posicao == '6':
                ultimo = corredor
        classif_final(primeiro, segundo, terceiro, quarto, quinto, ultimo)

    elif op == 's':
        colocacao = [primeiro, segundo, terceiro]
        colocacao.extend(ultimos_tres.values())

        trapaceiro = input('Quem trapaceou? :')
        vitima = input('Quem foi prejudicado? :')
        posicao_trapaceiro = colocacao.index(trapaceiro)
        posicao_vitima = colocacao.index(vitima)

        colocacao[posicao_trapaceiro] = vitima
        colocacao[posicao_vitima] = trapaceiro

        classif_final(*colocacao)

    else:
        print('Digite uma opção válida.')


def classif_final(*colocacao):
    for posicao, nome in enumerate(colocacao):
        print(f'{posicao + 1}a: {nome}')


print('-- CORREDORES --\n'
      'Mercúrio (MC)\nPapa-Léguas (PL)\nSonic (SN)\n'
      'Flash (FS)\nLigeirinho (LG)\nSuper Homem(SH)\n--------')
pri = input('Vencedor: ')
seg = input('Segundo: ')
ter = input('Terceiro: ')
qua = input('Quarto: ')
qui = input('Quinto: ')
ult = input('Último: ')

ultimos_tres = {'4': qua, '5': qui, '6': ult}

classif_parcial(pri, seg, ter, **ultimos_tres)
