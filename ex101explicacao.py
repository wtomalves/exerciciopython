def linha():
    """
    Função para imprimir print('_' * 30)
    faz uma linha reta
    :return: Sem retorno!
    Função criada por Wellington Alves aprendiz em programação
    """
    print('_' * 30)


print('''consultar a documentação, manual da linguagem no console python

help()

logo após digitar a função a ser consultada''')

linha()
print('''Consultar método dentro do Pycharm:

print(input.__doc__)

''')
linha()
# Criando uma docstring
print('''def linha():
    """
    Função para imprimir print('_' * 30)
    faz uma linha reta
    :return: Sem retorno!

    """
    print('_' * 30)resultado: ________________________.

    Agora mandando printar assim vai nos trazer as informações
    que eu coloquei a cima

    print(linha.__doc__)

    veja logo abaixo a informação disponibilizada''')

print(f'\033[34m{linha.__doc__}\033[m')
linha()


# parametros opicionais

def somar(a, b, c):
    s = a + b + c
    print(s)


somar(2, 3, 5)

print('''

def somar(a, b, c):
    s = a + b + c
    print(s)

somar(2, 3, 5)

RESULTADO = 10
---------------------------
AGORA...

def somar(a, b, c):
    s = a + b + c
    print(s)

somar(2, 3)

Mas se faltar um parametro como no exemplo acima 
vai dar erro. É aí que entra os parametros
opicionais:

Veja o exemplo sem alteração:

def somar(a, b, c):
    s = a + b + c
    print(s)

E agora com alteração: 

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(s)

somar(2, 3, 5)

Sendo assim também podemos passar para qual parametro
queremos, veja:

somar(a= 5, c= 2)

resultado = 7

...sem a necessidade de informamos o terceiro paramentro caso não queiramos.

      ''')

linha()
# Escopo de variáveis
print('''
Basicamente na progrmação escopo é o local onde uma variável vai existir, 
e o local onde ela nã vai existir:

Por exemplo:

Criar uma variável fora utilizarmos ela dentro de uma função... chamamos essa variável 
de variável global. 

Agora, quando se cria uma variável dentro de uma função que criamos, se você 
tentar ultilizá-la vai dar erro. <Chamamos de variável local>. O sistema mostrará a informação que a variável 
em questão não foi definida, tudo isso, porque ela foi criada dentro da função
que nós fizemos: 

exemplo:

def gato():
    animais = 'Quem não gosta de gatos são pessoas más!'
    print(animais)

gato()

resultado...''')
print('')


def gato():
    animais = 'Quem não gosta de gatos são pessoas más!'
    print(animais)


gato()
print()

print('''Agora se tentarmos printar essa variável na tela principal...

print(animais)
\033[31mNameError: name 'animais' is not defined\033[m''')
print()
print('''E para ultilizar a variável global é somente escrever global e o nome da variável. 
Se quiser atribuir outro valor na variável global pode. E consequentemente a isso o valor que original 
que a variável global possuia será apagado e substituído pelo novo valor atribuído''')

linha()
# ultilizando o Return

print('''Ultilizado para imprimir''')


def somar(a, b, c):
    s = a + b + c
    print(s)


somar(2, 3, 5)

print('''Agora com return

def somar(a, b, c):
    s = a + b + c
    return s

formulazinha = somar(2, 3, 5)

resultado será de 10

Basicamente no campo de return junto de variável s, o return vai retornar esse resultado 
para somar(2, 3, 5) que recebe o resultado dentro de uma variável nova, que chamamos de 
formulazinha ou simplesmente pedir para printar... print(somar(2, 3, 5))''')
print()


def somar(a, b, c):
    s = a + b + c
    return s


formulazinha = somar(2, 3, 5)

# print(formulazinha)
# print(somar(2, 3, 5))
linha()

'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        return f

n = int(input('Digite um número: '))
print(f' O fatorial de {n} é igual a {fatorial(n)}')'''


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))

if par(num):
    print('par')
else:
    print('Impar')
linha()


