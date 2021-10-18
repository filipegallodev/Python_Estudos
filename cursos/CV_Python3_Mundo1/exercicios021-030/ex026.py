frase = input('Digite uma frase: ')

print(f'Quantos "A" a frase possui: {frase.upper().count("A")}')
print(f'Posição em que aparece pela primeira vez: {frase.upper().find("A")}')
print(f'Em que aparece pela última vez: {frase.upper().rfind("A")}')
