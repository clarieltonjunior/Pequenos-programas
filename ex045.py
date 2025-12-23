from random import randint
import time

print('===SEJA BEM VINDO AO JOKENPO!!!=== \n')
print('''
Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
print('-=' * 20)
jogador = int(input('Qual Sua jogada?'))
#if jogador < 0 and jogador > 2:
 #   print('JOGADA INVALIDA')
print('PROCESSANDO...')
time.sleep(1.1)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)#TESTADO E FUNCIONANDO 
print('-=' * 12)
print('Computador jogou {}' .format(itens[computador]))
print('Jogador Jogou {}' .format(itens[jogador]))
print('-=' * 12)


if computador == 0:#PEDRA
    if jogador == 0:#PEDRA
        print('EMPATE')
    elif jogador == 1:#PAPEL
        print('JOGADOR VENCE')
    elif jogador == 2:#TESOURA
        print('JOGADOR PERDE')

if computador == 1:#PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')

if computador == 2:#TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')



