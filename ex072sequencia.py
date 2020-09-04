sequencia_numerica = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
nome_numerico = ('zero', 'um','dois','três','quatro','cinco','seis\n'
                ,'sete','oito','nove','dez','onze','doze','treze\n'
                ,'quartoze','quinze','dezesseis','dezessete','dezoito\n'
                ,'dezenove','vinte',)
digite = 0
digite = int(input('Digite um número: '))
cont = 0
if digite not in sequencia_numerica:
    while True:
        digite = 0
        digite = int(input('Digite novamente dentro da sequência de 0 a 20: '))
        if digite in sequencia_numerica:
            break

print(f'O número digitado foi {nome_numerico[digite]} ')





