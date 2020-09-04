salario = float(input('Calcule seu aumento salarial de 15%. Digite seu salario atual:'))
bonificacao = salario * 15 / 100
valoratualizado = salario + bonificacao
print('O valor do seu aumento foi de R${:.2f}! \nTotalizando o valor bruto de R${:.2f}!'.format(bonificacao, valoratualizado))