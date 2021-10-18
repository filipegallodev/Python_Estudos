num = int(input('Digite um número qualquer: '))

print(f'----- Tabuada do {num} -----')
for i in range(10):
    i += 1
    print(f'{num} x {i} = {num * i}')
