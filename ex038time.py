import time
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
print('...Comparando os dados...')
time.sleep(3)
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')



