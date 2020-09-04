viagem = float(input('Quantos km é a vigem?'))
custo1 = viagem * 0.50
custo2 = viagem * 0.45
if viagem <= 200.000:
    print('O custo da sua viagem será de R${:.2f}!'.format(custo1))
elif viagem >= 201.000:
    print('O custo da sua viagem será de R${}!'.format(custo2))
print('Boa viagem!')






















