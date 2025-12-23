'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

#Programa 35 Aprimorado

print('\nAnalise de segmentos')
r1 = float(input('\nInforme o comprimento do primeiro segmento: '))
r2 = float(input('Informe o comprimento do segundo segmento:  '))
r3 = float(input('Informe o comprimento do terceiro segmento:  '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos FORMAM UM TRIÂNGULO')
    if r1 == r2 and r2 == r3 and r3 == r1:
     print('Equilatero')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Escaleno')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Isósceles')