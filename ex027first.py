nome = input('Digite seu nome:').strip().upper().split()
print('O nome digitado é {}.\nFirst name: {}\nLast name: {}'.format(' '.join(nome), nome[0], nome[-1]))


