import random

numero = random.randint(0, 5)

tentativa = int(input('Tente adivinhar um número de 0 a 5: '))

if tentativa == numero:
    print('Você acertou! Parabéns!')
else:
    print('Você errou! Tente novamente!')
