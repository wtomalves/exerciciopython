def metade(p=0, show=False):
    resp = p / 2
    if show == True:
        return moeda(resp)
    else:
        return resp


def dobro(p=0, show=False):
    resp = p * 2
    if show == True:
        return moeda(resp)
    else:
        return resp


def aumentar(p=0 , desc_mais=0, show=False):
    resp = p + (p * desc_mais / 100)
    if show == True:
        return moeda(resp)
    else:
        return resp


def diminuir (p=0, desc_menos=0, show=False):
    resp = p - (p * desc_menos / 100)
    if show == True:
        return moeda(resp)
    else:
        return resp


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')


def resumo(p=0, desc_mais=0, desc_menos=0):
    print('*' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('*' * 30)
    print(f'dobro do preco: \t{moeda(p)}')
    print(f'metade do preço: \t{metade(p, True)}')
    print(f'O dobro do preço: \t{dobro(p, True)}')
    print(f'Aumentando {desc_mais}%: \t{aumentar(p, desc_mais, True)}')
    print(f'Reduzindo {desc_menos}%:  \t{diminuir(p, desc_menos, True)}')
    print('*' * 30)
