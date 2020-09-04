salario = float(input('Digite seu salário R$:'))
if salario >= 1250.00:
    print('Seu aumento será de 10% e o valor atualizado é de R${:.2f}!'.format((salario * 10 / 100) + salario))
if salario <= 1249.00:
    print('Seu aumento será de 15% e o valor atualizado é de R${:.2f}!'.format((salario * 15 /100) + salario))
