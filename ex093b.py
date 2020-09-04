
#neste daqui apliquei um while para que se o usuário
# digitar outro caracter apresente msg de erro
tabela = dict()
total_de_gols = list()
cont = 0
gols = 0
soma = 0

tabela['nome'] = str(input('Nome do Jogador:  ')).strip().capitalize()

while True:
    partidas = input(f'Quantas partidas {tabela["nome"]} jogou? ')
    if partidas.isnumeric():
        break
    else:
        print('Você não digitou caracter númerico, por favor digite novamente!')

while cont != int(partidas):
    cont += 1
    golss = input(f'Quantos gols na partida {cont}: ')
    if golss.isnumeric():
        gols = (int(golss))
        soma += gols
        total_de_gols.append(gols)
    else:
        print('Você não digitou caracteres númericos, digite outra vez!')
        cont += -1



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

