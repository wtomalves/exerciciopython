from datetime import date, datetime, timedelta #bibliotecas importadas
data = input('Digite sua data de nascimento ex 15/08/1996:')
data_de_nascimento = datetime.strptime(data, '%d/%m/%Y').date()#essa funcionalidade é para pegar a da fornecida pelo usuário e colocar na forma padrao que é ano, mes, dia.
padrao_nascimento = data_de_nascimento.strftime('%d/%m/%Y')# essa funcionalidade é para pegar a forma padrao de data de ano, mes, dia e passar para a forma de como lemos no Brasil que é dia, mes e ano
data_atual = date.today()
idade = data_atual - data_de_nascimento
anos = idade.days // 365
dias = idade.days % 365
mes = idade.days // 30 // anos

print('Analisando a data {} você tem {} anos!'.format(padrao_nascimento, anos))
if anos == 18:
    print('Você está na idade eletiva para o alistamento. Compareça a Junta MIlitar de sua cidade o quanto antes!')
elif anos >= 18:
        print('Você excedeu {} dias para alistamento militar. '.format(idade))
elif anos <= 17:
    print('Faltam precisamente {} dia(s) para o alistamento militar'.format(idade))
#o retorno vem com horário, não cnsegui remover. Quem sabe futuramente eu consiga

