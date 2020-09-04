primo = int(input('Digite um número: '))
vezes = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        vezes = vezes + 1

if vezes == 2: #Aqui estamos limitando ao computador apresentar somente os números divisivel por 1 e ele mesmo.
    print('Primo')
else: #Se a contagem do número analisado não maior que 2 nuúmeros divisiveis, então pode considerar que
    print('Não primo')                         #o número não é primo.

# "vezes = vezes + 1" Aqui toda vez que o número for divisivel por 0 vai ser contar 1
                 #independente de quantas vezes for. Todos os números tem como caracteristicas
            #serem divididos por 1 e por ele mesmo e tbm por demais números. Só que a característica
        #dos números primos é que eles somente são divisível por 1 e por ele mesmo.