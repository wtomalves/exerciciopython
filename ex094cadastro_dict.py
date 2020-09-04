cadastro = dict()
lista = list()
idades_somadas = maior = medio = menor = 0

while True:
    cadastro = {'nome': str(input('Nome: ')).strip().capitalize(),
                'sexo': str(input('Sexo: ')).strip().upper(),
                'idade': int(input('Idade: '))}
    lista.append(cadastro)
    continuar = str(input('Quer continuar: [S/N]')).strip()
    if continuar in 'Nn':
        break

print('===================================')
print(f'- O grupo tem {len(lista)} pessoas.')

for c in lista:
    idades_somadas += c["idade"]
media_das_idades = idades_somadas / len(lista)
print(f'- A média das idades é de {media_das_idades} anos')

print('- As mulheres cadastradas foram:', end='')
for c in lista:
    if 'F' in c['sexo']:
        print('(', c['nome'], ')', end=' ')

print()

print('- A lista das pessoas que estão acima da média:')
for c in lista:
    if c['idade'] >= media_das_idades:
        print(f' nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')
        print('')


