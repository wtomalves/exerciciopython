def leiaDinheiro(msg):
    ok = False
    valor = 0

    while True:
        n1 = input(msg).strip()
        n2 = n1.replace(',', '')
        n3 = n1.replace('.', '')

        if n2.isnumeric() or n3.isnumeric():
            if ',' in n1:
                n4 = n1.replace(',', '.')

            elif '.' in n1:
                n4 = n1.replace('.', '.')

            else:
                n4 = n1

            valor = float(n4)
            ok = True

        else:
            print(f'\033[31m"{n1}" não é um número inteiro válido!\033[m')

        if ok:
            break

    return valor
