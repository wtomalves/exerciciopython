import time
print('\033[32m$$$\033[31mBanco Real Cachorrinho\033[m\033[32m$$$\033[m')
print('')
cem = 100
cinquenta = 50
vinte = 20
dez = 10
um = 1
contador_cem = contador_cinquenta = contador_vinte = contador_dez = contador_um = 0
soma = 0
sacar = int(input('Deseja sacar quantos Cães em dinheiro? '))

print('')
print('PROCESSANDO...')
time.sleep(2)
print('')

print('Imprimindo valores em Cães...')
time.sleep(2)
print('')
while True:
    while soma < sacar and cem + soma <= sacar:
        soma += cem
        contador_cem += 1
    while soma < sacar and cinquenta + soma <= sacar:
        soma += cinquenta
        contador_cinquenta += 1
    while soma < sacar and vinte + soma <= sacar:
        soma += vinte
        contador_vinte += 1
    while soma < sacar and dez + soma <= sacar:
        soma += dez
        contador_dez += 1
    while soma < sacar and um + soma <= sacar:
        soma += um
        contador_um += 1
    if soma == sacar:
        break


print(f'"\033[31m{contador_cem}\033[m" Nota(s) de "R$100"\033[32m$Cães\033[m!')
print(f'"\033[35m{contador_cinquenta}\033[m" Nota(s) de "R$50" \033[32m$Cães\033[m!')
print(f'"\033[33m{contador_vinte}\033[m" Nota(s) de "R$20" \033[32m$Cães\033[m!')
print(f'"\033[34m{contador_dez}\033[m" Nota(s) de "R$10" \033[32m$Cães\033[m!')
print(f'"\033[32m{contador_um}\033[m" Nota(s) de "R$1"  \033[32m$Cão\033[m!')


