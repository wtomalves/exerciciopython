print('Cadastre seu peso!')
continuar = ''
dados = list()
registro = list()
quantas_pessoas = maior = menor = 0
nome_pessoa_mais_pesada = list()
nome_pessoa_menos_pesada = list()
peso1 = 0
peso2 = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: KG')))
    registro.append(dados[:])
    dados.clear()
    quantas_pessoas += 1
    continuar = str(input('Continuar? [S/N]?')).strip().upper()
    if continuar == 'N':
        break

print(f'foram cadastradas {quantas_pessoas} pessoas!')

while True:
    for p in registro:
        peso1 = p[1]
        if p[1] > 100 and maior == 0:
            maior = p[1]
        if peso1 >= maior:
            maior = peso1
            nome_pessoa_mais_pesada.append(p)



        else:
            peso2 = p[1]
            if p[1] < 99 and menor == 0:
                menor = p[1]
            if peso2 <= menor:
                menor = peso2
                nome_pessoa_menos_pesada.append(p)
    break

nomes1 = list()
for pessoa in nome_pessoa_mais_pesada:
    if pessoa[1] == maior:
        nomes1.append(pessoa[0])

nomes2 = list()
for pessoa in nome_pessoa_menos_pesada:
    if pessoa[1] == menor:
        nomes2.append(pessoa[0])


print(f'O maior peso é de {maior}Kg. Peso de {nomes1}')
print(f'O menos peso é de {menor}Kg. Peso de {nomes2}')
print('Fim')

