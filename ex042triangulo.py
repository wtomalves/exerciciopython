import time
print('DIGITE TRES RETAS EM CENTIMETROS E VERIFIQUE SE É POSSÍVEL FORMAR UM TRIANGULO!!!')
a = float(input('Digite lado "A": '))
b = float(input('Digite lado "B": '))
c = float(input('Digite lado "C": '))
print('Analisando os dados obtidos...')
time.sleep(3)

if a < b + c and b < a + c and c < a + b:
    print('Com os dados Digitados conseguimos formar um triângulo!')
else:
    print('Não foi possível formar triângulo com os dados digitados!')

if a == b == c:
    print('Triângulo Equilátero: Todos os lados são iguais!')
elif  a == b or a == c or b == c:
    print('Triangulo Isósceles: Dos lados iguais!')
else:
    print('Todos os lados são diferentes!')


