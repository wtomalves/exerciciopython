idade = homem = mulher_menor_20_anos = maior_idade = 0
genero = continuar = ''

while True:
    continuar = ''
    genero = ''
    idade = int(input('idade: '))
    while genero != 'F' and genero != 'M':
        genero = str(input('Genêro [M/F]: ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    if idade >= 18:
        maior_idade += 1
    if genero == 'M':
        homem += 1
    if idade <= 20 and genero == 'F':
        mulher_menor_20_anos += 1
    if continuar == 'N':
        break

print(f'"{maior_idade}" pessoa(s) tem a maior idade!')
print(f'"{homem}" pertence ao sexo masculino!')
print(f'"{mulher_menor_20_anos}" do sexo feminino tem menos de 20 anos!')
print('fim')








