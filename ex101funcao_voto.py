def situacao_De_voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Você tem {idade} anos! Não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos! Voto opcional!'
    else:
        return f'Você tem {idade} anos! Voto obrigatório!'

print('*' * 34)
print(" Análise sua situação de votação!")
print('*' * 34)

#programa principal
nascimento = int(input('Em que ano você nasceu? '))
print(situacao_De_voto(nascimento))

