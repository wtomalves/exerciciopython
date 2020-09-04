import random
import time
print('***' * 20)
print('Tente adivinhar o número que Madame Madelon está pensando!!!')
print('***' * 20)
sorteio = random.randint(0,5)
contador = 0
num = 6
while sorteio != num:
    num = int(input('Digite um número entre 0 a 5:'))
    print('PROCESSANDO...')
    time.sleep(0.5)
    sorteio = random.randint(0,5)
    contador += 1
    if num == sorteio:
        print('O número escolhido por você foi o mesmo de Madame Madelon, parabéns! E suas tentativas foram {} vezes.'.format(contador))
    else:
        print('Madame Madalon pensou em {}. Não foi dessa vez arrisque outro número!'.format(sorteio))
print('****JOGUEDENOVO****')