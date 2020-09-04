soma = 0
contador = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
        contador = contador + 1
        soma = soma + c #acomulador

print('A soma de todos os {} valores é {}!'.format(contador, soma))




