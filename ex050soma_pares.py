s = 0
for c in range(6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
print('A soma dos números pares são {}!'.format(s))
