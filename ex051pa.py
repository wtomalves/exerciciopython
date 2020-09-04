num = int(input('\nDigite o Primeiro termo da PA: '))
razão = int(input('Digite a Razão da PA: '))
for c in range(1, 11):
    print(num, end=' * ')
    num += razão
print('Acabou')


'''termo = int(input('\nDigite o Primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
decimo = primeiro + (10 - 1) * razao
contar_10_termos = 0
while contar_10_termos <= 10 -1:
      termo += razao
      print(termo - razao, end='  >  ')
      contar_10_termos += 1'''
