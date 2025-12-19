'''Faça um programa que leia uma frase pelo teclado
mostre quantas vezes aparece a letra “A”
em que posição ela aparece a primeira vez
em que posição ela aparece a última vez.'''



captura = str(input('Digite uma frase: '))

maiusculo_0 = captura.upper()
eliminar_espacos = maiusculo_0.strip()
frase = eliminar_espacos.replace(' ', '')

qtd_a = frase.count('A')
primeira_a = frase.find('A') +1
segunda_a = frase.rfind('A') +1



print('Quantidade de letras A : {}' .format(qtd_a))
print('Primeira letra A: {}' .format(primeira_a))
print('Segunda letra A: {}' .format(segunda_a))

