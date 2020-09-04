import moeda


preco = float(input('Digite um preço: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro do {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10% , temos {moeda.aumentar(preco, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13)}')
