import random

# valores = random.randint(0,10)
maior = menor = 0
contador = 0
dados = 0
for sorteio in range(5):
    contador += 1
    dados = random.randint(0, 10)
    print(f'Números selecionados {dados} na {sorteio + 1}º posição!')
    if dados < menor:
        menor = dados
    if dados > maior:
        maior = dados



print('')
print('----------------------------')

print(f'O Menor número sorteado é {(menor)}!')
print(f'O Maior número sorteado é {(maior)}!')
print('----------------------------')
print('')
print('\033[31mObservação:\033[m\n'
      '\n         Professor pediu para inserir os dados do sorteio'
      ' em uma única variável: Tupla. \n                    Mas nao consegui.'
      'Vou verificar a solução do professor!')
