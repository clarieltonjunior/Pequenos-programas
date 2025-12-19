# ==================================================
# PROGRAMA PARA VER SE É VIÁVEL COMPRAR UMA CASA
# EXERCÍCIO APRIMORADO PARA UM APP REAL
# PROGRAMADOR: CLARIELTON PEREIRA JUNIOR
# ==================================================

"""
Passo a Passo
1° Pergunta o valor da casa
2° Pergunta a renda total
3° Pergunta a quantidade de parcelas
4° Pergunta a taxa de juros
5° Só é viável se a parcela for <= 30% da renda
"""

import math

# =====================
# INTERFACE INICIAL
# =====================
print('Será que consigo pagar um imóvel?')

# =====================
# ENTRADA DE DADOS
# =====================
valor_casa = float(input('Valor da casa: R$'))
renda_total = float(input('Renda total: R$'))
parcelas = int(input('Número de parcelas: '))
porcentagem_juros = float(input('Porcentagem de juros: '))

# =====================
# CÁLCULO DOS JUROS
# =====================
ar = math.ceil(porcentagem_juros)   # Arredondamento para cima
juros = ar / 100                    # Conversão para porcentagem

total_com_juros = valor_casa + (valor_casa * juros)
valor_parcela = total_com_juros / parcelas

# =====================
# REGRA DOS 30% DA RENDA
# =====================
soma_renda_total = renda_total * 0.30

# =====================
# SAÍDA DE DADOS
# =====================
print('Valor da parcela: {:.2f} R$' .format(valor_parcela))
print('Valor ideal de parcela (30% da renda): R$', soma_renda_total)

# =====================
# ANÁLISE DE RISCO
# =====================
if soma_renda_total >= valor_parcela:
    print('Risco baixo para adquirir seu imóvel')
else:
    print('Risco alto, não compre!')
