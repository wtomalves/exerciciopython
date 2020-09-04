nomes = []
idades = []
generos = []
idade_homem_mais_velho = 0
feminino_menor_que_20_anos = 0
for registro in range(1,5):
    print('Cadastro número {}'.format(registro))
    print('')
    nome = input('Nome: ').strip().upper()
    idade = int(input('Idade: '))
    genero = input('Genero M/F: ').strip().upper()
    nomes.append(nome)
    idades.append(idade)
    if genero == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if genero == 'F' and idade < 20:
        feminino_menor_que_20_anos = feminino_menor_que_20_anos + 1


print('')
media_das_idades = (idades[0] + idades[1] + idades[2] + idades[3]) / 4
print('A média de idade do grupo é de {:.0f} anos.'.format(media_das_idades))
print('O homem mais velho é {}!'.format(nome_homem_mais_velho))

if feminino_menor_que_20_anos >= 1:
    print('{} mulher(es) tem menos de 20 anos!'.format(feminino_menor_que_20_anos))
else:
    print('Mediante aos seu dados fornecidos, não identificamos nenhum genero feminino abaixo dos 20 anos!')

print('ACABOU!!!')
