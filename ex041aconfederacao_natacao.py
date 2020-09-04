from datetime import date, datetime
print('Confederação de Natação! Verifique sua categoria! ')
data = input('Digite sua data de nascimento no modelo 00/00/0000: ')
data_de_nascimento = datetime.strptime(data, '%d/%m/%Y').date()
atual = date.today()
idade = atual - data_de_nascimento
anos = idade.days // 365
if anos <= 9:
    print('Categoria MIRIM!')
elif anos <= 14:
    print('Categoria INFANTIL!')
elif anos <= 19:
    print('Categoria JUNIOR!')
elif anos == 20:
    print('Categoria SENIOR!')
elif anos > 21:
    print('Categoria Master!')


