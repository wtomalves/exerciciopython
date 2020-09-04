numero = 0
quantidade = 0
soma = 0
pergunta = ''
lista = []
while pergunta != 'N':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    pergunta = input('Quer continuar [S/N]? ').strip().upper()
    soma += numero
    quantidade += 1

media = soma / quantidade
list.sort(lista)
print('A media dos valores digitados é {:.2f}!'.format(media))
print('O menor número é "{}" e o maior é "{}"!'.format(lista[0], lista[-1]))

