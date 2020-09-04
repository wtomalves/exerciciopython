from datetime import date

listas = list()

nomes = {'nome': str(input('Nome: '))}
listas.append(nomes)
ano_nascimento = {'ano': int(input('Ano de Nascimento: '))}
ano_atual = date.today().year - ano_nascimento['ano']
idade = {'idade': ano_atual}
listas.append(idade)
ano = date.today().year
anos_para_aposentar = 0
idade_1 = idade['idade']
while True:
    ctps = {'ctps': int(input('Carteira de Trabalho (0 se não tem: '))}
    listas.append(ctps)
    if ctps['ctps'] == 0:
        break
    else:
         contratacao = {'contratacao': int(input('Ano de Contratação: '))}
         listas.append(contratacao)
         salario = {'salario': float(input('Salário: '))}
         listas.append(salario)

         if contratacao['contratacao'] < ano:
             tempo_de_contribuicao = ano - contratacao['contratacao']
             anos_para_aposentar = 35 - tempo_de_contribuicao




    aposentado = {'aposentadoria': anos_para_aposentar + idade_1}
    listas.append(aposentado)

    break
print('************************')

for l in listas:
    for c in l.keys():
        for d in l.values():
            print(f'{c} tem o valor de {d}')