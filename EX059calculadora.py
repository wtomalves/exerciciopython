import time
maior = 0
menu = 0
while menu != 5:
    num1 = (int(input('Digite um valor: ')))
    num2 = int(input('Digite outro valor: '))
    print('')
    print('O que deseja fazer com os valores digitados?\n'
      ''
      '[1] Somar\n'
      '[2] Multiplicar\n'
      '[3] Maior\n'
      '[4] Novos números\n'
      '[5] Sair do programa\n')

    while menu != 5:
        menu = int(input('Digite a opção: '))
        if menu == 1:
            somar = num1 + num2
            print('A soma dos dois valores é {}!'.format(somar))
        if menu == 2:
            multiplicar = num1 * num2
            print('A multiplicação dos valores é {}!'.format(multiplicar))
        if menu == 3:
            if num1 > num2:
                maior = num1
            else:
                maior = num2
            print('O maior número é {}!'.format(maior))
        if menu == 4:
            print('Você optou por digitar novos valores!\n'
                  '>>> \033[31mAGUARDE\033[m <<<')
            time.sleep(5)
            num1 = (int(input('Digite um valor: ')))
            num2 = int(input('Digite outro valor: '))
print('Acabou!')