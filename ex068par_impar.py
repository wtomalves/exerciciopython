import random
print('******************')
print('Jogue Par ou Impar')
print('******************')
computador = random.randint(1,10)
soma = contador = 0
while True:
    usuario = int(input('Digite um número: '))
    escolha = str(input('Digite "P" para "PAR" ou "I" para "IMPAR"? ')).strip().upper()
    soma = computador + usuario
    par = soma % 2 == 0
    impar = soma % 2 != 0
    if par:
        print(f'Você escolheu {usuario} e o computador {computador}. Total de {soma}, portanto o resultado é Par.')

    if impar:
        print(f'Você escolheu {usuario} e o computador {computador}. Total de {soma}, portanto o resultado é Impar.')


    if escolha == 'P' and par or escolha == 'I' and impar:
        print('\033[35mUsuário venceu!\033[m')
        contador += 1
        print('')
    else:
        print('\033[31mComputador venceu!\033[m')
        break
print('')
print('************************************')
print(f'GAME OVER. E voce venceu {contador} vez(es)!')
print('************************************')