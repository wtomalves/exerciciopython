
sacola = ('tempestade', 'mozart', 'cachorrinho', 'bebechinho', 'papaizinho',
          'granola', 'caramelo','usina nucler',  'caneco', 'cinderela', 'liah bracho', 'teclado',
          'tela', 'computacao', 'programacao', 'python', 'javascript',
          'cinderela', 'ratatui', 'outono', 'caneco', 'estrogonofe', 'Igreja', 'ursulino')
print('=' * 40)
print('{:^40}'.format('VOGAIS'))
print('=' * 40)
for palavra in sacola:
    print(f'Vogal da palavra {palavra} é:', end=' ')
    if 'a' in palavra:
        print('A', end=' ')
    if 'e' in palavra:
        print('E', end=' ')
    if 'i' in palavra:
        print('I', end=' ')
    if 'o' in palavra:
        print('O', end=' ')
    if 'u' in palavra:
        print('U', end=' ')
    print('')