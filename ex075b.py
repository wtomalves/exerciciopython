núm = (int(input('Digite um número: ')), \
          int(input('Digite outro número: ')), \
          int(input('Digite mais um número: ')),\
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes!')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print(f'os números pares sao:', end= ' ')
for n in núm:
    if n % 2 == 0:
        print(f'{n}', end= ' ')


#Código do professor Guaná!


'''Considerações: Nestecódigo temos uma diminuição de linhas devido ao uso das funções:
núm.count(9) contar quantas vezes o número foi digitado.
{núm.index(3) fará a verificação em qual posição o número aparece.'''