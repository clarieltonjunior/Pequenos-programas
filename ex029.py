''' Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = int(input('Velocidade Detectada:'))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você foi multado!')
    print('Sua multa foi aproximadamente: R${:.2f}' .format(multa))
else:
    print('Liberado!')
