



def dados():
    import time

    arquivo = open('Dados_Salvos', 'r')
    print('=' * 50)
    print('PESSOAS CADASTRADAS'.center(50))
    print('=' * 50)
    for c in arquivo:

        print(f'{c}', end= '')

