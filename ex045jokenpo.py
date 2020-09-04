from random import choice
print(       '''       
      \033[33mJokenpô\033[m 

Jogue contra seu computador!''')
print('')
print('''OPÇÕES

      Pedra 
      PAPEL
      TESOURA ''')
print('')
usuario = input('Escreva uma das opções: ').upper().strip()
computador = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(computador)


print('')


if usuario == 'TESOURA' and computador == 'TESOURA':
     print('Ninguem venceu!')

if usuario == 'TESOURA' and computador == 'PAPEL':
    print('Você venceu!')

if usuario == 'TESOURA' and computador == 'PEDRA':
    print('Computador venceu!')

if usuario == 'PAPEL' and computador == 'PAPEL':
        print('Ninguem venceu!')

if usuario == 'PAPEL' and computador == 'PEDRA':
    print('Você venceu!')

if usuario == 'PAPEL' and computador == 'TESOURA':
    print('Computador venceu!')

if usuario == 'PEDRA' and computador == 'PEDRA':
     print('Ninguem venceu!')

if usuario == 'PEDRA' and computador == 'TESOURA':
         print('Você venceu!')

if usuario == 'PEDRA' and computador == 'PAPEL':
    print('Computador venceu!')


print('Você escolheu {} e computador escolheu {}!'.format(usuario, computador))

















