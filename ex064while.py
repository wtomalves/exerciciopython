stop = 999
number = 0
soma = 0
contador = 0
while number != stop:
    number = int(input('Digite um número: '))
    if number == stop:
        print('Você digitou "{}" número(s) e a soma dos números digitados foram "{}"!'.format(contador, soma))
    soma += number
    contador += 1

print('final')
