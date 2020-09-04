def ficha(n=0, g=0):
    if n == ''and g!= '': # valor de "n" não for digitado
        n = '<desconhecido>'
        return f'O Jogador {n} fez {g} gol(s) no campeonato.'

    elif n == '' and g == '': # nenhum valor for digitado
        n = '<desconhecido>'
        g = 0
        return f'O Jogador {n} fez {g} gol(s) no campeonato.'

    elif n != '' and g != '': # ambos valores digitados
        return f'O Jogador {n} fez {g} gol(s) no campeonato.'
    else:
        if n != '' and g == '': #valor de "g" não digitado
            g = 0
            return f'O Jogador {n} fez {g} gol(s) no campeonato.'



nome = input('Digite o nome do Jogador: ')
gols = input('Número de Gols: ')
print(ficha(nome, gols))




