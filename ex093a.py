tabela = dict()
total_de_gols = list()
cont = gols = soma = 0

tabela['nome'] = str(input('Nome do Jogador:  ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {tabela["nome"]} jogou? '))

while cont != partidas:
    cont += 1
    gols = int(input(f'Quantos gols na partida {cont}: '))
    soma += gols
    total_de_gols.append(gols)


tabela['gols'] = total_de_gols
print('*********************************************')
tabela['total'] = soma
print(tabela)
print('*********************************************')

for c, v in tabela.items():
    print(f' O campo {c} tem o valor {v}.')
print('*********************************************')
print(f'O jogador {tabela["nome"]} jogou {partidas} partidas.')

for c, v in enumerate(tabela["gols"]):
    print(f'=> Na partida {c + 1}, fez {v} gols.')

print(f'Foi um total de {tabela["total"]} gols.')








