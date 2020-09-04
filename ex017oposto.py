import math
oposto = float(input('Digite o comprimento do cateto oposto:'))
adjacente = float(input('Digite o comprimento do cateto adjacente:'))
hipotenusa = math.hypot(oposto,adjacente)
print('O cumprimento da hipotenusa é {:.1f} centímetros!'.format(hipotenusa))
    