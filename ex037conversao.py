import time
num = int(input('Digite um número inteiro: '))
print('...Guardando suas inforções, um momento por favor...')
time.sleep(5)
conversao = input('Agora escolha a base de conversão:  \nDigite 1 para "BINÁRIO", 2 para "OCTAL" e 3 para "HEXADECIMAL: ')
print('...Realizando a transformações de dados...')
time.sleep(5)
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)
if conversao == '1':
    print('Número inteiro digitado "{}", base de conversão escolhida "{}" sua conversão binária é "{}"!'.format(num, conversao, binario))
elif conversao == '2':
    print('Número inteiro digitado "{}", base de conversão escolhida "{}" sua conversão octal é "{}"!'.format(num, conversao, octal))
elif conversao == '3':
    print('Número inteiro digitado "{}", base de conversão escolhida "{}" sua conversão hexadecimal é "{}"!'.format(num,conversao, hexadecimal))



