'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import radians, sin, cos, tan
an = float(input('Ângulo: '))
sin = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))

print('Sen: {:.2f} Cos:{:.2f} Tan: {:.2f}' .format(sin, cos, tan))
