dias = float(input('Quantos dias de aluguel do carro?'))
kilometro = float(input('Quantos kilometros percorridos?'))
custos = (dias * 60) + (kilometro * 0.15)
print('valor total do aluguel pelos dias e kilometragem rodada é de R${:.2f}!'.format(custos))




