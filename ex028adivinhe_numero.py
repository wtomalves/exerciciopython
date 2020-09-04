import random
import time
print('***' * 20)
print('Tente adivinhar o número que Madame Madelon está pensando!!!')
print('***' * 20)
num = int(input('Digite um número entre 0 a 5:'))
print('PROCESSANDO...')
time.sleep(2)
sorteio = random.randint(0,5)
if num == sorteio:
    print('O número escolhido por você foi o mesmo de Madame Madelon, parabéns!')
else:
    print('Madame Madalon pensou em {}. Não foi dessa vez arrisque outro número!'.format(sorteio))
print('****JOGUEDENOVO****')
