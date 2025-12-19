'''Escreva um programa que faça o computador “sortear” em um número inteiro entre 0 e 5 e peça para o
   usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random


computador = random.randint(0,5)

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5 tente advinhar, BOA SORTE!')
print('-=-' * 20)

jogador = int(input('\nEm que numero eu pensei? \n'))

if jogador == computador:
     print('Parabens você GANHOU!')
else:
    print('-=-' * 20)
    print('Eu pensei em {} e você em {} NÃO FOI DESTA VEZ !!!' .format(computador, jogador))
    print('-=-' * 20)
