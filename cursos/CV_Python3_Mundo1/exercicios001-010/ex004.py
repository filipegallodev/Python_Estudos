valor = input('Digite algo: ')

print(f'Tipo primitivo da variável: {type(valor)}')
print(f'É numérico? {valor.isnumeric()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'É decimal? {valor.isdecimal()}')
print(f'Está todo em maiúsculo? {valor.isupper()}')
print(f'Está todo em minúsculo? {valor.islower()}')
