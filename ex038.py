'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''


numero = int(input('Primeiro Numero:'))
numero2 = int(input('Segundo Numero:'))

if numero < numero2:
    print('Segundo numero é maior')
elif numero > numero2:
    print('Primeiro numero é maior')
else:
    print('Os numeros são iguais')