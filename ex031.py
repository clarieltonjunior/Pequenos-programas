'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''


import time

pessoas = int(input('Digite seu numero de viajantes: '))
time.sleep(0)#Tempo de espera
print('===' *20)
print('PROCESSANDO...')

print('===' *20)#divisor
time.sleep(1)

kms = float(input('Distancia da viagem em km: '))
menor200 = 0.50 * kms
maior200 = 0.45 * kms
taxa_pessoa = pessoas * 35

print('===' *20)
print('PROCESSANDO...')
time.sleep(1)

if kms <= 200:
    print('total da viagem: R$ {}' .format(menor200 + taxa_pessoa))
else:
    print('total da viagem: R$ {}' .format(maior200 + taxa_pessoa ))