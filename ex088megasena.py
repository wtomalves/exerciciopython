import random
import time
print('=' * 50)
print(' '*15,'JOGO DA MEGA SENA')
print('=' * 50)

lista = []

cont = rodada = 0
vezes = int(input('Quantos jogos você quer que eu sorteie? '))


print('Carregando as Informações...')
time.sleep(2)
print()
print(f'*SORTEANDO {vezes} JOGOS*')
time.sleep(2)
print('     AGUARDE...')

print()
while cont != vezes:
    rodada += 1
    jogo = []
    sorteados = 0
    while sorteados != 6:
        sorteio = random.randint(1, 60)
        if sorteio not in jogo:
            jogo.append(sorteio)
            sorteados += 1
    jogo.sort()
    lista.append(jogo)

    cont += 1



rodada = 1
for c in lista:
    time.sleep(1.5)
    print(f'Jogo {rodada}:{c}')
    rodada += 1

print()
print('Boa Sorte!')

