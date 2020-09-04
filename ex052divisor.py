n = int(input('Digite um número:'))
divisor = n > 1 and n % n == 0 and n % 2 != 0
if divisor:
    print('{} é um numero primo!'.format(n))
if n == 2:
    print('{} é um numero primo!'.format(n))
else:
    print('O número {} não é primo.'.format(n))