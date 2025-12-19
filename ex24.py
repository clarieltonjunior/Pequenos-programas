'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''

# 1. Solicita o nome da cidade ao usuário
# 2. Limpa a entrada: remove espaços em branco e converte para maiúsculas
# 3. Verifica se as 5 primeiras letras são "SANTO"
# Usamos fatiamento ([:5]) para pegar os primeiros 5 caracteres


cid = str(input('Nome da cidade:'))
remov_espaco = cid.strip()
mai = remov_espaco.upper()

print(mai[:5] == 'SANTO')


