''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random

a1 = str(input('1° Aluno: '))
a2 = str(input('2° Aluno: '))
a3 = str(input('3° Aluno: '))
a4 = str(input('4° Aluno: '))
lista = [a1, a2, a3, a4]
i = bool(input('Iniciar Sorteio?'))#Acrescentar sim ou não

al = random.choice(lista)
print('\nO aluno escolhido foi {}' .format(al))