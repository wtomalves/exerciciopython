def mostrarlinha():
    print('-'* 25)

def calculo(*num):
    print(f'A largura = {largura} x comprimento = {comprimento}')
    formula = largura * comprimento
    print(f'A área do terreno é {formula}m²')

print('Calculando m² de terrenos:')
mostrarlinha()

largura = float(input('Largura: '))
comprimento = float(input('Comprimento:' ))
calculo(largura, comprimento)









