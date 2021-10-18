import random

nomes = list(range(4))

for i in range(4):
    nomes[i] = input(f'Digite o {i+1}º nome do aluno: ')
    i += 1

print(f'O aluno escolhido para apagar a lousa é o(a) {random.choice(nomes)}!')
