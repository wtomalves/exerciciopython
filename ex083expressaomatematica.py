operacoes_basicas = 0
sequencia_de_numeros = 0
colc_aspas_chaves = 0
operadores_matematicos = ['+', '-', '*', '/','%', '//']
expressao_matematica = ['(', ')', '{', '}', '[', ']']
sequencia_numerica = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
expressao = input('Digite uma expressão númerica: ')

for c in expressao:
    if c in sequencia_numerica:
        sequencia_de_numeros += 1

    if c in expressao_matematica:
        colc_aspas_chaves += 1

    if c in operadores_matematicos:
        operacoes_basicas += 1


if sequencia_de_numeros <= 1:
    print('erro1')
else:
    if colc_aspas_chaves % 2 != 0:
        print('erro2')
    else:
        if operacoes_basicas <= 0:
            print('erro3')
        elif len(expressao.split('++')) > 1:
            print('erro3')
        elif len(expressao.split('--')) > 1:
            print('erro3')
        elif len(expressao.split('**')) > 1:
            print('erro3')
        elif len(expressao.split('//')) > 1:
            print('erro3')
        elif len(expressao.split('////')) > 1:
            print('erro3')
        elif len(expressao.split('%%')) > 1:
            print('erro3')


        else:
            if len(expressao.split('()')) > 1:
                print('erro4')
            elif len(expressao.split('[]')) > 1:
                print('erro4')
            elif len(expressao.split('{}')) > 1:
                print('erro4')
            else:
                print('temos a expressão matemática!')


#Não consegui chegar na efucácia de uma equação e sua totalidade






