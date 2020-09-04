

#PARA CADASTRAR PESSOAS

def PessoasCadastradas():
    import time
    time.sleep(0.5)
    arquivo = open(f'Dados_Salvos', 'a')
    print('=' * 50)
    print('{:^50}'.format('NOVO CADASTRO'))
    print('=' * 50)
    nome = str(input('Nome: '))
    while True:
        try:
            idade = int(input('Idade: '))

        except (ValueError, TypeError):
            print('\033[31mERRO---> Digite um número inteiro!\033[m')
            continue

        print(f'\033[34mNovo registro de {nome} adicionado!\033[m')
        print()
        arquivo.writelines(f'{nome:<30}')#escreve no arquivo
        arquivo.writelines(f'{idade:>15}\n')  # escreve no arquivo


        arquivo.close



        break





