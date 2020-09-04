numero = int(input('\nDigite o Primeiro termo da PA: '))
termo = numero
razao = int(input('Digite a Razão da PA: '))
contar_10_termos = 0
while contar_10_termos <= 10 -1:
    print(termo, end=' > ')
    termo += razao
    contar_10_termos += 1
print('')
pergunta = ''
while pergunta != 'S' and pergunta != 'N':
    pergunta = str(input('\nQuer continuar [S/N]: ')).upper()
    if pergunta == 'N':
        print('Você optou por não continuar. Agradecemos pela participação!')
    if pergunta == 'S':
        print('')
        pergunta = int(input('Você optou por continuar!\n.'
                             'Digite quantos termos a mais quer que o computador imprima? '))
        contar_10_termos = 0
        termo = numero
        while contar_10_termos != pergunta + 10:
            print(termo, end=' > ')
            termo += razao
            contar_10_termos += 1
