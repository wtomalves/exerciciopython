#Selecionar um elemento do dicionário:
pessoas = {'nome':'Cachorrinho', 'Sexo': 'M', 'idade': '02'}
print(pessoas['nome'])
print('*************')

#Selecionar dois elementos ou mais:
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} aninhos!')
#Neste caso temos que colocar aspas duplas para não dá erro!
print('*************')

#Selecionar as chaves:
print(pessoas.keys())
print('*************')

#Selecionar os valores:
print(pessoas.values())
print('*************')

#Selecionar todas as informações do dicionários:
print(pessoas.items())
print('*************')

#Acessando por estrutura de laçõs:
for k in pessoas.values():
    print(f'O {k} é somente meu! ')
    break
print('*************')

#Todos os valores
for k in pessoas.values():
    print(k)
print('*************')

#todos as chaves:
for k in pessoas.keys():
    print(k)
print('*************')

#todas as chaves e valores juntos:
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('*************')

#Adicionar mais um item:
pessoas['Peso'] = 9.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('*************')

#Criando dicionário dentro de uma lista:
brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {"uf": 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])#Aqui acessamos a lista e conseguimos acessar também o
print('*************')

estado = dict()
brasil = list()
for c in range(0,2):
    estado['uf'] = str(input('Unidade Federativa: ')).strip().capitalize()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip().upper()
    #Vamos ultilizar o método .Copy(). Senão criamos a cópia o resultado final
    #será a informação do ultimo laço.
    brasil.append(estado.copy())

print(brasil)
print('*************')

#Apresentar por Estado e UF:
for e in brasil:
    print(e)
print('*************')

#Apresentar os Estados junto com siglas:
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
print('*************')











