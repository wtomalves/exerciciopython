valores = []
menor = maior = cont_menor = cont_menor = 0
for numero in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    if numero == 0:
        menor = valores[numero]
        maior = valores[numero]
    if valores[numero] < menor:
        menor = valores[numero]
    if valores[numero] > maior:
        maior = valores[numero]


print(f'Os números digitados foram {valores}')
print(f'O menor número é {menor} e foi encontrado na posição:', end=' ')
for cont, numero in enumerate(valores):
    if numero == menor:
        print(f'{cont}...', end='')

print('')
print(f'O maior número é {maior} e foi encontrado na posição:', end=' ')

for cont, numero in enumerate(valores):
    if numero == maior:
        print(f'{cont}...', end=' ')
