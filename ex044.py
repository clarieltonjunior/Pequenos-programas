''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros '''

#BIBLIOTECAS
import time

#ENTRADA DE DADOS
v_original = float(input('Valor do Produto: '))
print('PROCESSANDO...')
time.sleep(1)

#VARIAVEIS
a_vista = v_original - (v_original * 0.10)
av_cartao = v_original - (v_original * 0.05)
two_card = v_original / 2
v_vezes = v_original + (v_original * 0.20) 

f_pagamentos = print('''
[1] Pagamento á vista
[2] Pagamento á vista no cartão
[3] Pagamento  2x
[4] Pagamento em 3x ou mais 
''')                    

forma_pag = int(input('Selecione a opção de pagamento:'))

if forma_pag == 1:
    print('Valor a pagar {:.2f}' .format(a_vista))
elif forma_pag == 2:
    print('Valor a pagar {:.2f} em duas vezes' .format(av_cartao))
elif forma_pag == 3:
    print('Valor a pagar {:.2f}' .format(two_card))
elif forma_pag == 4:
    print('Valor a pagar {:.2f}' .format(v_vezes))
else:
    print('Sua forma de pagamento esta invalida!')