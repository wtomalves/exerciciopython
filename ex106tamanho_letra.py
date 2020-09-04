
def linha(msg):
    tamanho = len(msg)
    print('*' * tamanho)
    print(f'  {msg}  ')
    print('*' * tamanho)


def me_explique(duvida):
        import time
        print(f'\033[42:31m')
        linha(f'\033[42:31mAcessando o manual do comando "{opcao}"')
        time.sleep(1)
        print('\033[40:35m')
        return help(duvida)


while True:
    print(f'\033[44:30m')
    linha('\033[44:30mSistema de Ajuda PyHelp')
    opcao = input('\033[mFunção ou Biblioteca >').strip().lower()

    if opcao == "fim":
        linha('\033[46:31mAté logo')


        break
    print(me_explique(opcao))













