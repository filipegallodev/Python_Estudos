from math import radians, sin, cos, tan

angulo = radians(float(input('Digite o valor do ângulo: ')))

print(f'O valor do Seno deste ângulo é: {sin(angulo):.2f}')  # :.2f limita as casas para 2 depois do .
print(f'O valor do Cosseno é: {cos(angulo):.2f}')
print(f'O valor da Tangente é: {tan(angulo):.2f}')
