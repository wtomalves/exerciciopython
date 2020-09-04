def leiaInt():
    while True:
            try:
                n = int(input('Digite um número inteiro: '))
            except:
                    print('\033[31mDigite um número inteiro válido!\033[m')
                    continue
            else:
                return n



def leiafloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except:
            print('\033[31mDigite um número inteiro válido!\033[m')
            continue
        else:
            return n



print(f'O valor inteiro digitado foi {leiaInt()} e o real foi {leiafloat()}')
