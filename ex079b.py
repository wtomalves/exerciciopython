sequencia = []
while True:
    numero = int(input('Digite um valor:'))
    if numero not in sequencia:
        sequencia.append(numero)
        print('Valor adicionado')
    else:
        print('Identificamos que já digitou este número!')
    resposta = str(input('Continuar [S/N]? '))
    if resposta in 'Nn':
        break

print('')
sequencia.sort()
print(f'os números digitados foram: {sequencia}')

'''Em pesquisa no web, me deparei com a informação que em Python
tem o "set" que realizada a função de eliminar os numeros repetidos'''


