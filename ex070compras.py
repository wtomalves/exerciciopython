
print('\033[35mCompras On_Line!!!\033[m')
print('')
produto = menor_produto = continuar = ''
menor_preco = contar = preco = soma = 0
while True:
    produto = continuar = ''
    preco = 0
    produto = str(input('Nome do produto: '))
    preco = float(input('Valor do produto: R$'))
    if menor_preco == 0:
        menor_preco = preco
    if preco < menor_preco:
        menor_preco = preco
        menor_produto = produto

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Continuar compras [S/N]: ')).strip().upper()
    if preco >= 1000.00:
        contar += 1
    soma += preco

    if continuar == 'N':
        break
print('')
print('\033[31mInformações da compra!\033[m')
print(f'Valor total de gasto nas compras é de R${soma:.2f}!')
print(f'"{contar}" produto(s) custa(m) mais de R$1.000,00!')
print(f' O produto mais barato é "{menor_produto}" e seu valor é de {menor_preco:.2f}!')