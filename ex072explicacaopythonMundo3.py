lanche = ('Laranja', 'Chocolate', 'Chantily', 'Granola')
#Tuplas são imutáveis
#lanche[2] = 'Flango Flito' ERRO (não podem ser íténs atribuídos)

for c in lanche:
    print(f'Eu vou comer {c}')
print('{:-^30}'.format('Outra forma'))

for c in range(0, len(lanche)):
    print(lanche[c])
print('{:-^30}'.format('Outra forma'))

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')
print('{:-^30}'.format('Outra forma'))

for item, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {item}')
print('{:-^30}'.format('Outra forma'))
print('Mostrar os iténs em ordem alfabética')
print(sorted(lanche))
print('{:-^50}'.format('-'))


print('Comi pra caramba!')
print('{:-^50}'.format('-'))
print('{:-^50}'.format('-'))
print('{:-^50}'.format('-'))

a = (2, 5, 4)
b = ( 5, 8, 1, 2)
c = a + b
print('''a = (2, 5, 4)
b = ( 5, 8, 1, 2)
c = a + b''')
print('Resultado:')
print('Juntar uma Tupla "A + B" e atribuir na "C":', (c))
print('Quantos elementos tenho na Tupla :',len(c))
print('Quantas vezes está aparecendo o nº 5?', c.count(5), 'vez(es)!')
print('Em que posição está o número 8 considerando a ordem' , c,':\nEstá na posição nº', c.index(8))
print('\033[31mMas preste atenção neste detalhe:\033[m')
print('Se tiver dois números iguais dentro da Tupla considerando este exemplo (2, 5, 4, 5, 8, 1, 2), '
      'e você quiser\nverificar somente um, deve informar'
      'a posição para iniciar a pesquisa. Porque se não informar, ele seleciona\n'
      'o primeiro número que encontra.\nConsiderando'
      ' a posição 0, 1, 2... Ex: \033[36mc.index(5)\033[m resultado: \033[35mPosição 1\033[m.')
print('Agora se você informar de qual indice a pesquisa deve partir, por exemplo:\n'
      '>>>\033[36mc.index(5, 2)\033[m<<< resultado: \033[32mPosição 3\033[m.')
print('{:-^50}'.format('-'))
print('{:-^50}'.format('-'))
print('{:-^50}'.format('-'))
print('Mais uma explicação referente as Tuplas:')
dados_pessoais = 'Tom', 30, 'M', 126.40
print(dados_pessoais)
print('Se eu utilizar del(dados_pessoais) ele apagará as informações que foram definidas.\n'
      'Por exemplo: \033[33mdel(dados_pessoais)\033[m', 'mensagem: \033[31mNome dados_pessoais não está definido!\033[m')

