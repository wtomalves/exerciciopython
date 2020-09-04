 #MEU CÓDIGO MELHORADO
from datetime import date

cadastro = dict()

cadastro['Nomes'] = str(input('Nome: ')).strip().capitalize()
cadastro['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = ((cadastro['Contratação'] + 35) - date.today().year) + cadastro['Idade']

print('##########################')
for c, v in cadastro.items():
    print(f'{c} tem o valor {v} ')


