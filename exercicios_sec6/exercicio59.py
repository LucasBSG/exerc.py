import random

aleatorio = random.randint(1,10)

palpite = int(input('Adivinhe o número: '))

if aleatorio == palpite:
    print('Você acertou, o número é: %d' % aleatorio)
else:
    print('Você errou, o número é: %d' % aleatorio)