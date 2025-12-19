'''O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome'''



nome = input('Digite seu nome completo: ')

maior = nome.upper()
menor = nome.lower()
nome_sem_espacos = nome.replace(" ", "") #Retirando espaços em branco para contagem de characteres
pnome = nome.split()

print('\nMaior: {}'.format(maior))
print('Menor: {}'.format(menor))
print('Quantidade de letras sem espaço: {}'.format(len(nome_sem_espacos)))
print('Quantidade de letras com espaços: {}' .format(len(nome)))
print('Primeiro Nome: {}' .format(len(pnome[0])))
print('Primeiro Nome: {}' .format(pnome[0]))

