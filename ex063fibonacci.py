'''Sequência de FIBONACCI'''
'''fomula fn + fn + 1 = fn + 2
Isso quer dizer que se você pega um número de Fibonacci qualquer
'fn' é soma ao seu sucessor 'fn + 1', o resultado da soma é
'fn + 2', que quer dizer... o sucessor, do sucessor. fn1 = 1 e fn2 = 1 (teremos sempre
que partir dessa base. Em sequência
para obter o fn3, é somar fn1 + fn2. ou seja: fn3 é 2. Para o fn4 somariamos o fn2 + fn3 e 
seu resultado é 5. E assim sucessivamente.'''
fibonacci = int(input('Digite um numero: '))
fibonacci_0 = 0
fibonacci_1 = 1
soma = 1
sequencia_inicial = 0
while sequencia_inicial <= fibonacci - 1:
    print(soma)
    soma = fibonacci_0 + fibonacci_1
    fibonacci_0 = fibonacci_1
    fibonacci_1 = soma
    sequencia_inicial += 1





