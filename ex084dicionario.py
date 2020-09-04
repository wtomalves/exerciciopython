teste = list()
teste.append('Guaná')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Tomzinho'
teste[1] = 30
galera.append(teste[:])
print(galera)
print('---------------------------------')
galera = [['Tempestade', 3],['Mozart', 2], ['Caramelo', 0]]
print(galera)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade!')
print('-----------------------------')
galera = list()
dados = list()
maior = menor = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        menor += 1
print(f' Temos {maior} maiores de idade e {menor} menores de idade!')
