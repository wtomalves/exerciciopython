s = quantidade = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    quantidade += 1

print(f'Foram digitados {quantidade} números e a soma dos valores é {s}!')

