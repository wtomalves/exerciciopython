
'''try: #para tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: #se der erro
    #Utilizamos o Exception e criamos uma variável ERRO
    #e conseguimos imprimir o tipo de erro pelo __class__
    print('Infelizmente tivemos um problema')
    print(f'O problema encontrado foi {erro.__class__}')

else: #quando der certo
    print(f'O resultado é {r:.1f}')
finally:#independente de acerto ou falha
    print('Fim')'''

print()
print()
print('''Podemos tratar os erros e determinando o tipo de erro e a informação que
queremos passar ao usuário, ou até mesmo ao programador no momento de
criação do código, veja o exemplo abaixo:''')

print()

try: #para tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: #quando der certo
    print(f'O resultado é {r:.1f}')
finally:#independente de acerto ou falha
    print('Fim')

print()
print()



