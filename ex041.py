#ler ano de nascimento
#mostrar em qual categoria ele se encaixa
#
'''Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER'''

from datetime import date

ano = int(input('Qual ano do seu nacimento? '))
atual = date.today().year
idade = atual - ano

if idade <= 9 :
    print('Classificação: Mirim')
    print('Sua idade é {}'.format(idade))

elif idade >= 9 and idade < 14:
    print('Classificação: Infantil')
    print('Sua idade é {}'.format(idade))

elif idade >= 14 and idade < 19:
    print('Classificação: Junior')
    print('Sua idade é {}'.format(idade))

elif idade >= 19 and idade < 25:
    print('Classificação: Sênior')
    print('Sua idade é {}'.format(idade))

elif idade >= 25:
    print('Master')
    print('Sua idade é {}'.format(idade))
