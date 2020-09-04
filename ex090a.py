dados = dict()
for c in range(0, 1):
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    dados['media'] = float(input(f'Média de {dados["nome"]}: '))

print(f'Nome é igual a {dados["nome"]}\nMédia é igual a {dados["media"]}')

if dados['media'] > 6.0:
    print('Situação é igual a Aprovado!')
else:
    print('Situação é igual a Reprovado!')

print('Fim')


print()

