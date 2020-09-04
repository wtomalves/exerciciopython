import time

cadastro = dict()

def linha():
    print('=' * 30)


def contador(inicio):
    print(f'Contagem de {comeco} até {final} de {pulo} em {pulo}')

    # imprimir o ultimo valor reistrado no cadastro['fim']
    # quando cadastro['passo'] é negativo
    if cadastro['inicio'] > cadastro['fim'] and cadastro['passo'] <= -1:
        cadastro['fim'] += cadastro['passo']

    # imprimir os valores descrecente quando o inicio é maior
    # que o fim.
    if cadastro['fim'] < cadastro['inicio'] and cadastro['passo'] >= 1:
        cadastro['fim'] = cadastro['fim'] - cadastro['passo']
        cadastro['passo'] = - cadastro['passo'] * 1

    # imprimir de forma descrescente
    if cadastro['passo'] <= -1:
        cadastro['passo'] = + cadastro['passo']

    # imprimir quando o passo for zero
    if cadastro['passo'] == 0:
        cadastro['fim'] = (cadastro['fim'] - 1) - cadastro['passo']
        cadastro['passo'] = - cadastro['passo'] * 1
        cadastro['passo'] = -1



    for c in range(inicio['inicio'], inicio['fim'], inicio['passo']):
        print(c, end=' ')
        time.sleep(0.5)


linha()
print('Contagem de 1 até 10 de 1 em 1')
time.sleep(0.5)
for c in range(1, 11, 1):
    print(c, end=' ')
    time.sleep(0.5)

print()
print('Contagem de 10 até 0 de 2 em 2')
time.sleep(0.0)
for c in range(10, -1, -2):
    print(c, end=' ')
    time.sleep(0.5)

print()
linha()
print('Agora é sua vez de personalizar a contagem!')

cadastro = {'inicio': int(input('Digite um numero: ')),
            'fim': int(input('Fim: ')),
            'passo': int(input('Passo: '))}


inalteravel = (cadastro['inicio'], cadastro['fim'], cadastro['passo'])
comeco = inalteravel[0]
final = inalteravel[1]
pulo = inalteravel[2]


linha()

contador(cadastro)

