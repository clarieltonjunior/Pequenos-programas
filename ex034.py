'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''


salario = float(input('Valor do salario: '))
s1 = salario * 0.10 #aumento para salario acima de 1250
total1 = salario + s1
s2 = salario * 0.15 #aumento para salario abaixo de 1250
total2 = salario + s2

if salario <= 1250:
    aumento = total2
    print('Novo Salario: R$ {:.2f}'.format(aumento))
else:
    aumento = total1
    print('Novo Salario: R$ {:.2f}'.format(aumento))



