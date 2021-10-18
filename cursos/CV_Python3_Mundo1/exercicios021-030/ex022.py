nome = input('Digite seu nome completo: ')

print(f'Com as letras maiúsculas: {nome.upper()}')
print(f'Com as letras minúsculas: {nome.lower()}')
print(f'Tamanho do nome completo: {len(nome.replace(" ",""))} letras')
nome = nome.split()
print(f'Tamanho do primeiro nome: {len(nome[0])} letras')
