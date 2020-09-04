import moeda


p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro do {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10% , temos {moeda.aumentar(p, 10,)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')



