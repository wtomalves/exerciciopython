print('***' * 7)
print('Para formarmos um triângulo é necessário tres retas de diferentes centimentos. \nContudo podemos ter dificuldade para a formação de triângulo devido a algumas regras. \nPara saber se os dados que você possui conseguira realizar um triangulo, por favor forceça dos dados!,')
print('***' * 7)
a = int(input('Digite o primeiro número lado "a":'))
b = int(input('Digite o segundo número lado "b":'))
c = int(input('Digite o terceiro número lado "c":'))
if a < b + c and b < a + c and c < a + b:
    print("Com esses dados conseguimos fazer um triângulo!")
else:
   print(' Com esses dados não conseguimos formar um triângulo!')

