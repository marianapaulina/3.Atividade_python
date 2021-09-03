'''Gerar um número de 1 a 100, e solicitar para que o usuário tente adivinhar o número'''

numero = 46

chute = int(input(' Digite um numero:'))

print(' voce digitou: {}'. format(chute))


acertou = chute == numero


if(acertou):
    print('voce acertou')
else:
 print('voce errou')

