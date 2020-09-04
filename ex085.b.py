num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('=' * 40)
num[0].sort()
num[1].sort()
print(f'Os números pares são: {num[0]}')
print(f'Os números impares são: {num[1]}')
