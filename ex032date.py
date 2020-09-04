from datetime import date
ano = int(input('Verifique se é ano bissexto, ou digite 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(' O ano {} digitado é bissexto!'.format(ano))
else:
    print('O número {} digitado "NÂO" é bissexto!'.format(ano))

