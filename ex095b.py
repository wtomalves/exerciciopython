#código melhorado com sucesso kkkk
tabela = dict()
jogadores = list()
soma = cont = informacoes = posicionamento_na_tabela = 0

while True:
    tabela = {'nome': str(input('Nome do Jogador: ')).strip().capitalize()}
    jogadores.append(tabela)
    partidas = int(input(f'Quantas partidas {tabela["nome"]} jogou? '))
    tabela['gols'] = []
    for c in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {c + 1}: '))
        tabela['gols'].append(gol)
    continuar = str(input('Quer continuar: [S/N]'))
    print('=' * 51)
    if continuar in 'Nn':
       break

print('{:^4}{:^10}{:^25}{:^20}'.format('Cód','Nome', 'gols', 'Total'))
print('=' * 51)

for c, v in enumerate(jogadores):
    nome = str(v["nome"])
    gol = str(v["gols"])
    soma = sum(v["gols"])
    print(f'{c:^4} {nome:^9} {gol:^24} {soma:^16}')

print('_' * 50)

while True:

    informacoes = int(input('Mostrar dados de qual Jogador? [999] sair '))
    if informacoes == 999:
        print('VOLTE SEMPRE!')
        break

    for posicionamento_na_tabela, jogador_individual in enumerate(jogadores):
        cont += 1
        if informacoes == posicionamento_na_tabela:
            cont = 0
            print(f'--LEVANTAMENTO DO JOGADOR {jogador_individual["nome"]}:')
            for posicao, gol_individual in enumerate(jogador_individual["gols"]):
                print(f'  No jogo {posicao} fez {gol_individual} gols')

        else:
            if cont == len(jogadores):
                print(f'"ERRO" Não existe jogador com código {informacoes} tente novamente!')
                print('==============================================')

