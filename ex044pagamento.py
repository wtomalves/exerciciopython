print('''Condições de pagamento:

  1- À vista e/ou cheque com 10% de desconto;
  2- À vista no cartão com 5% de desconto;
  3- Em 2x sem juros no cartão;
  4- A partir de 3x no cartão com 20% de juros;''')
print('')

opcao = int(input('Selecione a opão desejada e aperte enter: '))
preco = float(input('Digite o valor a ser pago R$:'))
print('')

if opcao == 1:
    print('Valor total á vista de R${:.2f}!'.format(preco- (preco * 10 / 100)))
elif opcao == 2:
    print('Valor total á vista de R${:.2f} no cartão!'.format(preco - (preco * 5 /100)))
elif opcao == 3:
    print('02 parcelas no valor sem juros de R${:.2f}!'.format(preco / 2))
elif opcao == 4:
    parcelamento = int(input('Digite a quantidade de parcelas:'))
    print('Parcelamento em {} vezes no valor de R${:.2f}!'.format(parcelamento, (preco * 20 / 100 + preco) / parcelamento))
    print('\033[31mEvite entrar em atraso, nossos valores e correções monetárias são atualizados diariamente!')