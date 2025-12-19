'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nome = input('Digite seu nome: ')
nom = nome.upper()
nom1 = nom.split()

print('SILVA' in nom1)