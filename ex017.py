'''faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triangulo retangulo e calcule e mostre o comprimento da hipotenusa'''

import math
co = float(input('\nValor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = math.hypot(co, ca)

print('\nComprimento da hipotenusa: {:.2f} ' .format(hi))
print('\nObrigado por utilizar nossos sistemas!')



