'''for c in range(1,11):
    print(c)          (usado somente quando eu sei o limite)
print('FIM')'''

'''c = 1
while c < 11:   
    print(c)   #Usado também quando eu sei o limite, assim como no for in range()
    c += 1'''


'''numero = 1
while numero != 0:
    numero  = int(input('Digite um valor: '))
print('FIM')    #Usado também quando eu não sei o limite'''

'''letra = 'S'
while letra == 'S':
    numero = int(input('Digite um número: '))
    letra = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM') #podemos criar situações de laços indeterminado'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} números pares e {} números impares!'.format(par, impar))

