nome = input('Escreva uma frase:').strip().lower()
print('Quantas vezes aparece a letra "A"? {} vez(es)!'.format(nome.count('a')))
print('Em que posição a letra "A" aparece a primeira vez? Na {} posição!'.format(nome.find('a')))
print('Em que posição a letra "A" aparece por ultimo? Na {} posição!'.format(nome.find('a', -1)))




