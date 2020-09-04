
def metade(p=0):
    resp = p / 2
    return resp


def dobro(p=0):
    resp = p * 2
    return resp


def aumentar(p=0 , desc=0):
    resp = p + (p * desc/ 100)
    return resp


def diminuir (p=0, desc=0):
    resp = p - (p * desc / 100)
    return resp


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')


'''criamos uma função com nome de moeda. 
O outro moeda entrou como paramentro
por exemplo: moeda='R$: se eu não informar a moeda,
o parametro a moeda será o real,No final formatamos 
e trocamos o ponto pela virgula'''



