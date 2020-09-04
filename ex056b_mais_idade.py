somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range (5):
    print('------ {} ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1


mediaidade = somaidade / 4
print('A média das idades é {} anos!'.format(mediaidade))
print('O homeme mais velho tem {} e se chama {}!'.format(maioridadehomem, nomevelho))
print('Ao todo temos {} do sexo feminino a baixo de 20 anos!'.format(totalmulher20))


#Código realizado pelo professor Guanabara!
