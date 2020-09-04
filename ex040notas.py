n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media >= 9.0:
    print('Sua média é de {:.1f}! Parabéns!'.format(media))
elif media >= 6.0:
    print('Sua média é de {:.1f}! Muito bom. Parabéns!'.format(media))
elif media >= 4.0:
    print('Sua média é de {:.1f}! faltou pouco para conseguir, mas não foi dessa vez!'.format(media))
elif media >= 0.0:
    print('Sua média é de {:.1f}! Média baixissíma! Estude Mais!'.format(media))
print('Boa Sorte!!!')
