import random

nomes = list(range(4))

for i in range(4):
    nomes[i] = input(f'Digite o {i+1}º nome: ')
    i += 1

random.shuffle(nomes)
print(f'A ordem de apresentação para o trabalho é: ')
print(nomes)
