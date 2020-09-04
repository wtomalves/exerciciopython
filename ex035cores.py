nome = input('\033[1;35mDigite seu nome:').strip().upper().split()
print('\033[31m{} \033[35m{} \033[36m{} \033[33m{} \033[34m{} \033[37m{} \033[30m{} \033[32m{} '.format(nome[0], nome[1], nome[2], nome[3], nome[4], nome[5], nome[6], nome[7]))

print('\033[1;31;43mOlá, mundo!')
#Podemos utilizar no final da mensagem o \033[m para delimitar a modificação.
print('\033[m---Veja no exemplo abaixo---')
print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[m---Veja no exemplo abaixo---')
print('\033[34mOlá, mundo!')