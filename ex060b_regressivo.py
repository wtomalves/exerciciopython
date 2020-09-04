num = int(input('Digite um valor: '))
resultado = 1
for c in range(num, 1, -1):
    resultado = resultado * c
print(float(resultado))
