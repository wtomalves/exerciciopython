print('SIMULAÇÃO IMOBILIÁRIA >>> Verifique a possibilidade para concessão de empréstimo:')
casa = float(input('Qual o valor da casa? '))
salario = float(input('qual o valor da renda mensal? '))
anos = int(input('Em quantos anos deseja quitar o financiamento? '))
parcela = casa / (anos * 12)
limite = salario * 30 / 100
if parcela <= limite:
    print('Parabéns, com os dados fornecidos vocÊ tem um crédito pré-aprovado!')
else:
    print('Infelizmente com os dados fornecidos não é possível solicitar o financiamento. \nEm casos de dúvidas procure sua agência!')









