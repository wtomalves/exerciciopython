def notas(*n, show=False):
    '''

    -> Função para análisar notas e situações
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param show: se True mostra a situação das notas do grupo
    :return: dicionário com várias informações sobre a situação da turma
    Criado por Tom Alves
    '''
    cont = 0
    for c in sorted(n):

        cont += 1
        if cont == 1:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c


    if show==False:
        resp = {'total':len(n), 'maior': maior, 'menor': menor, 'media': sum(n) / len(n)}
        return resp
    else:
        if show == True:
            media = sum(n) / len(n)
            if media <= 4:
                situacao = 'Ruim'
            elif media <= 6:
                situacao = 'Razoável'
            elif media < 10:
                situacao = 'Bom'
            else:
                situacao = 'Ótimo'

            resp = {'total': len(n), 'maior': maior, 'menor': menor, 'media': sum(n) / len(n), 'Media': situacao}
            return resp


resp = notas(1, 5, 30, show=True)
print(resp)
help(notas)
