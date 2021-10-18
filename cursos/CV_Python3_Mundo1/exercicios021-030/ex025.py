nome = input('Digite seu nome completo: ')

nome = nome.upper()
print(f'O nome possui "SILVA"?')

if nome.find("SILVA") >= 0:
    print('Sim')
else:
    print('Não')
