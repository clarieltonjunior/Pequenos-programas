'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

print('\nAnalise de segmentos')
r1 = float(input('\nInforme o comprimento do primeiro segmento: '))
print('-' * 40)
r2 = float(input('Informe o comprimento do segundo segmento:  '))
print('-' * 40)
r3 = float(input('Informe o comprimento do terceiro segmento:  '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('-=' * 20)
    print('Os segmentos FORMAM UM TRIÂNGULO')
    print('-=' * 20)
else:
    print('NÃO FORMA TRIÂNGULO')