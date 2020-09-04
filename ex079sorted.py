sequencia = []
while True:
    sequencia.append(int(input('Digite um valor: ')))

    if sequencia:
        continuar = str(input('Continuar [S/N]: ')).strip().upper()
    if continuar == "N":
        break

print('')
print('os números digitados foram:',sorted(set(sequencia)))











'''Em pesquisa no web, me deparei com a informação que em Python
tem o set que realizada a função de eliminar os numeros repetidos'''


