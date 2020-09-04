
nota = []
aluno_e_nota = []
boletim = []

while True:
    aluno = str(input('Nome: ')).capitalize()
    aluno_e_nota.append(aluno)
    nota_1 = float(input('Nota 1: '))
    nota.append(nota_1)
    nota_2 = float(input('Nota 2:'))
    nota.append(nota_2)

    media = (nota_1 + nota_2) / 2
    aluno_e_nota.append(media)


    aluno_e_nota.append(nota[:])
    nota.clear()
    boletim.append(aluno_e_nota[:])
    aluno_e_nota.clear()

    media = 0

    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break

print('=' * 40)
print('{:-^40}'.format('Boletim'))
print('=' * 40)


for posicao, nome in enumerate(boletim):
    print(f'Nº: \033[33m{posicao}\033[m    Aluno: \033[34m{nome[0]}\033[m    Média: \033[31m{nome[1]}\033[m')

consultas = 0
while True:
    consultas = int(input('Digite o Nº da tabela acima e obtenha as notas do aluno ou 999 para sair:  '))
    if consultas == 999:
        break
    for posicao, nome in enumerate(boletim):
        if consultas == posicao:
            print(f'Nº: \033[33m{posicao}\033[m    Aluno: \033[34m{nome[0]}\033[m    NOtas: \033[31m{nome[2]}\033[m')


print('Finalizando...')
print('Volte sempre!')


