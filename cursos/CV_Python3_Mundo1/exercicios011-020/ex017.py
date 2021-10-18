from math import hypot

catop = float(input('Digite o comprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))

print(f'O comprimento da hipotenusa é: {hypot(catop, catadj)}')
