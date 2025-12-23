peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual sua Altura em (m)? '))
imc = peso / (altura * altura)
print('Seu IMC é de {:.2f}: ' .format(imc))

if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Você esta com o peso Ideal')
elif  imc > 25 and imc < 30:
    print('Você esta com Sobrepeso')
elif imc > 30 and imc < 40:
    print('Você esta com Obesidade')
elif imc > 40:
    print('Obesidade Mórbita')