velocidade = float(input('Qual a velocidade do carro?'))
multa = (velocidade - 80) * 7
if velocidade >= 81.0:
    print('Voce excedeu a quilometragem permitida! Valor de multa a ser paga é de R${:.2f}!'.format(multa))
else:
    print('Você não excedeu a quilometragem permitida, parabéns!')
print('Desejamos lhe uma boa viagem!')