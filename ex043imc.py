import time
print('Calcule seu Índice de Massa Corperea!')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite a altura '))
imc = peso / (altura * altura)
print('...Calculando seu IMC...')
time.sleep(3)

print('Seu IMC é de {:.1f}!'.format(imc))

if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso ideal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 34.9:
    print('Obesidade grau I')
elif imc <= 39.9:
    print('Obesidade grau II')
elif imc >= 40:
    print('Obesidade mórbida grau III')
print('')

print('Veja a Tabela: ')

print('')

print('''Resultado:
	   
	   CLASSIFICAÇÃO	OBESIDADE          (GRAU)
	   
       MENOR QUE          18,5	          MAGREZA	     
       ENTRE           18,5 E 24,9	       NORMAL         
       ENTRE           25,0 E 29,9	     SOBREPESO	     
       ENTRE           30,0 e 34,9       OBESIDADE I    
       ENTRE           30,0 E 39,9	     OBESIDADE II
       MAIOR QUE          40,0	       OBESIDADE GRAVE III''')





