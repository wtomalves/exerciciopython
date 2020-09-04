print('Criação de uma variável')
num = [2,5,9,1]
print('num = [2,5,9,1]')
print(num)
print('------------------------')
print('Substituindo o índice 2')
num[2]= 3
print('num[2]= 3')
print(num)
print('------------------------')
print('Adcionando o valor 7')
print('num.append(7)')
num.append(7)
print(num)
print('------------------------')
print('Ordenanação crescente')
print('num.sort()')
num.sort()
print(num)
print('------------------------')
print('Ordenação descrente')
print('num.sort(reverse=True)')
num.sort(reverse=True)
print(num)
print('------------------------')
print('Contar quantos elementos')
print('{len(num)}')
print(f'Essa lista tem {len(num)} elementos')
print('------------------------')
print('Inserir um elemento')
print('num.insert(2, 0)')
num.insert(2, 0)
print(num)
print('------------------------')
print('Remover ultimo elemento')
print('num.pop()')
num.pop()
print(num)
print('------------------------')
print('Remover escolhendo o indice')
print('num.pop(2)')
num.pop(2)
print(num)
print('------------------------')
print('Remover elemento usando IF:')
print('num = [7, 5, 3, 2]')
print('''if 4 in num:
    num.remove(4)
else:
    Não achei o número 4
Resultado:''')
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print('------------------------')
print('Apresentação da lista')
print('''valores = []
valores.append(5)
valores.append(9)
valores.append(4) ''')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
print('Agora usando formatação ')
print(''' for v in valores:
    print(f'{v}...')'
resultado: ''')
for v in valores:
    print(f'   {v}...')
print('se quiser na mesma linha')
print('Usar, end=" "')
for v in valores:
    print(f'{v}...', end=' ' )
print('')
print('------------------------')
print('Achar a posição')
print(''' for c, v in enumerate(valores):
    print(f' Na posição {c} encontrei  o valor {v}!') 
Resultado:''')
for c, v in enumerate(valores):
    print(f' Na posição {c} encontrei  o valor {v}!')
print('---------------------------------------------')
print('Ler valores pelo teclado e a adcionar a lista')
print('''for cont in range(0,5):
    valores.append(int(input('Digite um valor: '))) ''')
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print('Resultado: ')
print(valores)
print('')
print('Agora com a posição: ')
for c, v in enumerate(valores):
    print(f' Na posição {c} encontrei  o valor {v}!')
print('-----------------------------------')
print('Em Python as listas tem ligação' )
print('''a = [2, 3, 4, 7]
b = a
b[2] = 8
resultado: ''')
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista A: {b}')
print('----------------------')
print('criar uma cópia em lista sem ligação ')
print('Na variável b = a acrescentamos [:]')
print('''Ou seja:'
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
resultado:''')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista A: {b}')
print('----------------------')


