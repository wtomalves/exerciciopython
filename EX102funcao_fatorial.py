def fatorial(n, show=False):
    """
    -> Calcule um fatorial de um número.
    para n1: O número a ser calculado.
    para show: (opcional). Mostrar ou não a conta.
    :return: O valor do fatorial de um número.
    Criado por Tom Alves.
    """

    if show == True:
        f = 1
        cont = 0
        for c in range(n, 0, -1):
            f *= c
            print(f'{c}', end= ' ')
            while cont != 4:
                cont += 1
                print('x', end= ' ')
                break

        print(end= '= ')
        return f

    else:
         if show == False:
             f = 1
             for c in range(n, 0, -1):
                f *= c


             return f


print(fatorial(5))
print()
help(fatorial)
