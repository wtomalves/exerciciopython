from operator import itemgetter
import random
import time


jogador = {}
lista = []
jogador = {'nome': "jogador1", 'nota': random.randint(1, 6)}
lista.append(jogador)
jogador = {'nome': "jogador2", 'nota': random.randint(1, 6)}
lista.append(jogador)
jogador = {'nome': "jogador3", 'nota': random.randint(1, 6)}
lista.append(jogador)
jogador = {'nome': "jogador4", 'nota': random.randint(1, 6)}
lista.append(jogador)

print('Valores sorteados!')
for c, jogador_na_lista in enumerate(lista):
    time.sleep(2)
    print(f'  O jogador{c + 1} tirou {jogador_na_lista["nota"]}')


ranking = sorted(lista, key=itemgetter('nota'), reverse=True)


time.sleep(1)
print('Ranking dos Jogadores:')


for posicao, jogador in enumerate(ranking):
    print(f'  {posicao + 1}º lugar: {jogador["nome"]} ')
    time.sleep(2)


