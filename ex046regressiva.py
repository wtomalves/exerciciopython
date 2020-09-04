import time
estouro = input('Dê tecla enter para iniciar a contagem regressiva dos fogos de artifícios: ')
print('Contagem regressiva em...')
time.sleep(2)

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)

for c in range(0,2):
    print('''\033[31mBOOMM!
    BOOMM!
        BOOMM!''')
    time.sleep(0.3)







