print('Digite 7 números e verifique se são pares ou impares!')
lista = list()
par = list()
impar = list()
for c in range(1,8):
    num = int(input(f'Digite o número {c}º: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

lista.append(par)
lista.append(impar)
lista[0].sort()
lista[1].sort()
print(f'Os números pares são: {lista[0]}')
print(f'Os números impares são: {lista[1]}')




