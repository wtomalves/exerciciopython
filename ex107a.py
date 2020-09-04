'''from numeros import fatorial, dobro, triplo


num = int(input('Digite um número: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O dobro de {num} é {triplo(num)}')'''


import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

def metade(m):
    resp = m / 2

    return resp


v = float(input('N: '))
print(f'{locale.currency(metade(v), grouping=True)}')
