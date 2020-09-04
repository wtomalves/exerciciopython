#palíndromo: Palavra ou frase que pode ser lida de traz pra frente idependente de espaços na frase.
#Ex: "A base do teto desaba" == "abased otet od esab A"
frase = input('Digite uma frase:').strip().upper()
frase_quebrada = frase.split()
frase_juntada = ''.join(frase_quebrada)
quantidade_de_caracteres = len(frase_juntada)
ultima_posicao = quantidade_de_caracteres - 1
frase_invertida = ''
for c in range(ultima_posicao, - 1, - 1):
    frase_invertida = frase_invertida + frase_juntada[c]

if frase_invertida == frase_juntada:
    print('Essa frase é um Palíndromo!')
else:
    print('Essa frase "NÃO" é um Palíndromo!')

'''
Minha busca para a solução desse problema não foi linear, isso porque ao
escrever o código fiz várias modificações. Os espaços da direita e esquerda foram
faclmente removidos pela funcionalidade strip, mas os espaços entre a frase não. Então precisei
remover. Consegui isso utilizando a funcionalidade split que teve a função de renomear
o possicionammento a partir de cada espaço. logo após precisei juntar toda a frase, e por isso
utilizei o ''.join. que ealizado desta forma agora tenho a cantagem de caracter mas sem contar
os espaços. Daí com a funcionalidade Len pude obter a quatidade daquilo que eu precisava (fiz este
processo porque quando eu escrevia a frase, mesmo sendo um palindromo, o sistema não reconhecia).
Criei essa variavel "ultima_posicao" para que meu sistema pudesse comparar as palavras do final
para o começo.
 O for c in range(ultima_posicao, - 1, - 1): criei foi pelo raciocinio que:
o programa verificaria a frase do final ao começo do final ao passo decrescente de -1.

Por exemplo:

CASA DE MADAME MADELON - NOLEDAM EMADAM ED ASAC

                   OU

A BASE DO TETO DESABA - ABASED OTET OD ESAB A

A variavel frase_invertida = '' foi criada para realizar o processo de concatenação. Além
disso o que foi feito foi reconstruir a frase de tras para frente, letra por letra e 
salvar as letras de trás para frente para o sistema comparar: 

ex: A BASE DO TETO DESABA 
    A BASE DO TETO DESABA - ABASEDOTETODESABA
    ABASEDOTETODESABA (17 caracteres)
    ABASEDOTETODESABA (ultima posição é 16)
    ABASEDOTETODESABA >>> Analisando de tras pra frente
    frase_invertida = '' + ABASEDOTETODESABA == 'ABASEDOTETODESABA'
    Por fim a Condição de Se ABASEDOTETODESABA é igual a 'ABASEDOTETODESABA'
    
    '''






