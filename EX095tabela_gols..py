#primeiro código mas não ficou tao bom e alguns erros
tabela = dict()
total_de_gols  = list()
total = list()

soma = 0

while True:
        tabela = {'nome': str(input('Nome do Jogador: ')).strip().capitalize()}
        total_de_gols.append(tabela)
        partidas = int(input(f'Quantas partidas {tabela["nome"]} jogou? '))


        for c in range(0, partidas):
            gols = int(input(f'Quantos gols na partida {c + 1}: '))
            total_de_gols.append(gols)

        total.append(total_de_gols[:])
        total_de_gols.clear()


        continuar = str(input('Quer continuar: [S/N]'))
        if continuar in 'Nn':
            break


print('==============================================')
print('{:^5}{:^15}{:^15}{:^15}'.format('Cod', 'nome', 'gols', 'total'))
print('==============================================')

for c, v in enumerate(total):
    soma = sum(v[1:])
    gol = str(v[1:])
    print(f'{c:} {v[0]["nome"]:^15} {gol:^15} {soma:^15}')

print('==============================================')

informacoes = 0
while True:
    for v in total:
        if informacoes == 999:
            break
        for c, v in enumerate(total):
            informacoes = int(input('Mostrar dados de qual Jogador? [999] sair '))
            if informacoes == 999:
                print('VOLTE SEMPRE!')
                break

            if informacoes == c:
                print(f'--LEVANTAMENTO DO JOGADOR {v[0]["nome"]}:')

                for c, d in enumerate(v):
                    if c > 0:
                        print(F'  No jogo {c} fez {d} gols.')

            else:
                print(f'"ERRO" Não existe jogador com código {informacoes} tente novamente!')
                print('==============================================')
        break

