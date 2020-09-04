from ex115.cadastro import pessoas, dados
import time


while True:
    time.sleep(0.5)
    try:

        print('=' * 50)
        print('Menu Principal'.center(50))
        print('=' * 50)

        print('''
        \t\t1 - ver cadastrados
        \t\t2 - cadastro novo
        \t\t3 sair do sistema''')
        print('=' * 50)
        time.sleep(0.5)
        opcao = int(input('Opção: '))

        if opcao == 1:
            dados.dados()

        elif opcao == 2:
            pessoas.PessoasCadastradas()

        elif opcao == 3:
                print('*' * 50)
                break
    except:
        print('*' * 50)
        print('\033[31mDigite uma opção válida!\033[m'.center(50))
        print('*' * 50)





print('\033[31mSaindo do istema...Até logo!\033[m'.center(50))
print('*' * 50)
time.sleep(0.5)





