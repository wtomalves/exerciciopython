def escreva(msg):
    tamanho = len(msg) + 2
    print('=' * tamanho)
    print(f' {msg}')
    print('=' * tamanho)


frase = str(input('Escreva uma frase: '))
escreva(frase)

