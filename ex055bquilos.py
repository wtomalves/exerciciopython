quilos = []
for c in range(5):
    quilos.append(float(input('Digite seu peso: ')))

list.sort(quilos)

print('Menor peso é {} e maior peso é {}!'.format(quilos[0], quilos[-1]))

#list.sort(quilos) coloca a lista ordenada do menor para o maior
