genero = ''
while genero != 'F' and genero != 'M':
    genero = str(input('Gênero [M/F]: ')).upper()
    if genero == 'F':
        print('Seu gênero é FEMININO!')
    if genero == 'M':
        print('Seu gênero é MASCULINO!')
print('FIM')