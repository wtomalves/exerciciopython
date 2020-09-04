from Tools.scripts.which import msg


# criando uma função
def mostrarLinha():
    print('_' * 30)


caozinho = 'Cachorrinho LIndo'
mostrarLinha()
print(f'{caozinho:^30}')
mostrarLinha()


# criando um parametro
# aqui conseguimos personalizar
# ainda mais o programa
def gatinhos(msg):
    print('_' * 30)
    print(f'{msg:^30}')
    print('_' * 30)


gatinhos('Mozart e Temprestade')


# imprimindo mais de um titulo
def titulo(txt):
    print('_' * 30)
    print(f'{txt:^30}')
    print('_' * 30)


titulo('Bebechino')
titulo('Chitos')
titulo('Caramelo')
mostrarLinha()


# criando função matematica


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    mostrarLinha()


print('Printando a soma:')

soma(3, 2)
soma(4, 7)
soma(10, 10)
mostrarLinha()

print('''POdemos alterar o ordem do numero de A para B:
Exemplo:
A = 3
B = 2
podemos declarar assim:
soma(b=3, a=2)
resultado =  A = 2 e B = 3 = soma de 5''')
mostrarLinha()


# Empacotamento
def contador(*num):  # colocmos este asteriosco que significa desempacotar
    # que siginifica que independente do parametro que o usuário digitar
    # é para pegar todos os números e jogar dentro de num
    for valor in num:
        print(f'{valor}', end='  ')
    print()


print('''def contador(*num): #colocmos este asteriosco que significa desempacotar
    # que siginifica que independente do parametro que o usuário digitar
    # é para pegar todos os números e jogar dentro de \033[31mnum\033[m''')

print('''criou uma tupla:
contador(2, 3, 4)
contador(9, 8, 10)
contador(5, 7, 1, 6)''')

print()

print('''usandp for no def'
for valor in num:
print(f'{valor}', end='  ')
print()')''')

contador(2, 3, 4)
contador(9, 8, 10)
contador(5, 7, 1, 6)
mostrarLinha()


# contado número
def contando(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')


print('Contando números:')
contando(2, 3, 4)
contando(9, 8, 10)
contando(5, 7, 1, 6)
mostrarLinha()



# Dobrando os valores dentro de uma lista
def dobra(lst):
    pos = 0
    while pos < len(lst):#Enquanto posição for menor que o tamanho da minha lista
        lst[pos] *= 2
        pos += 1



print('Imprimindo o dobro dos valores = [2, 6, 8, 4, 1, 5]')
valores = [2, 6, 8, 4, 1, 5]
dobra(valores)
print(valores)

print('''
# Só para entender o que está acontecendo aqui:
# Eu passei como parametro lista valores = [2, 6, 8, 4, 1, 5] e em dobra(valores)
# passamos essa lista. Então neste momento vamos ter duas listas na memoria. Uma lista chamada
# valores e outra chamada lst. Exemplo: def dobra(lst). E tudo o que eu fizer em lst vai interferir
# em valores. Resumindo quando eu chamar o dobra(valores) ele vai pegar [2, 6, 8, 4, 1, 5] e vai dobrar
# os números sucessivamente''')
mostrarLinha()
mostrarLinha()
