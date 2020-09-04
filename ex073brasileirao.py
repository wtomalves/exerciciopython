print('{:=^16}'.format(''))
print('Brasileirão 2020')
print('{:=^16}'.format(''))
ordem_colocacao  = ('Flamengo', 'Atlético-MG',
'Botafogo', 'Bahia',
'Palmeiras', 'Vasco'
'Santos', 'Bragantino',
'Corinthians', 'Atlético-GO',
'Grêmio', 'Fluminense',
'Sport', 'Ceará',
'Coritiba', 'Internacional',
'Fortaleza', 'Athletico',
'Goiás', 'São Paulo')

print('Lista do TIme do Brasileirão: Nº1 Flamengo,', 'Nº2 Atlético-MG,',
'Nº3 Botafogo,', 'Nº4 Bahia,',
'Nº5 Palmeiras,', 'Nº6 Vasco,'
'Nº7 Santos,', 'Nº8 Bragantino,',
'Nº9 Corinthians,', 'Nº10 Atlético-GO,',
'Nº11 Grêmio,', 'Nº12 Fluminense,',
'Nº13 Sport,', 'Nº14 Ceará,',
'Nº15 Coritiba,', 'Nº16 Internacional,',
'Nº17 Fortaleza,', 'Nº18 Athletico,',
'Nº19 Goiás e ', 'Nº20 São Paulo')
print('')
print(f'Os 5 primeiros colocados são: {ordem_colocacao[0:5]}')
print('')
print(f'Os 4 últimos colocados da tabela são: {ordem_colocacao[-4:]}')
print('')
print(f'Segue os times em ordem alfabética: {sorted(ordem_colocacao)}')
print('')
print('\o/')
