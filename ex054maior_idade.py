from datetime import date
atual = date.today().year
maior = 0
menor = 0

for ano in range(7):
    data_de_nascimento = int(input('Data de nascimento: '))
    idade = atual - data_de_nascimento
    if idade >= 18:
        maior = maior + 1
    if idade <= 17:
        menor = menor + 1

print('Das datas analisas {} pertence a maior idade e {} a menor idade!'.format(maior, menor))
