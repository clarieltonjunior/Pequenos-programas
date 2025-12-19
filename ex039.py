'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date

#=================
#Entrada de Dados
#=================

nome = str(input('Qual seu nome: '))
ano = int(input('Qual seu ano de nascimento: '))
idade = int(input('Qual sua idade: '))

if idade <18 or idade > 65:
    print('Você não pode se alistar!')
elif idade == 18:
    print('Você ja pode se alistar!')
elif idade > 18 and idade < 65 :
    print('Você Ja passou da data de alistamento!')
else:
    print('')