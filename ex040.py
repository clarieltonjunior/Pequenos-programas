#PROGRAMA DE MÉDIAS
#3 NOTAS 
#REPROVADO|RECUPERAÇÃO|REPROVADO

#BIBLIOTECAS
import math

#VARIAVEIS

nome = str(input('Nome do aluno:'))
n1 = float(input('1° Nota: '))
n2 = float(input('2° Nota: '))
n3 = float(input('3° Nota: '))

soma = n1 + n2 + n3
media = soma / 3

if media < 5:
    print('Você foi REPROVADO!')
elif media >= 5  and media <= 6.91:
    print('Você está em RECUPERAÇÃO!') #FUNCIONANDO
elif media > 7:
    print('Aprovado!Boas Festas!') #FUNCIONANDO




