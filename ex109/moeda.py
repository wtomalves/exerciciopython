
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



def aumentar(p=0 , desc=0, show=False):
    resp = p + (p * desc/ 100)
    if show == True:
        return moeda(resp)
    else:
        return resp


def diminuir (p=0, desc=0, show=False):
    resp = p - (p * desc / 100)
    if show == True:
        return moeda(resp)
    else:
        return resp


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')






