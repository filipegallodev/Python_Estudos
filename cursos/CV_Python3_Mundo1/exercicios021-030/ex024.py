cidade = input('Digite o nome de uma cidade: ')

cidade = cidade.upper().split()
print(f'O nome da cidade começa com "SANTO"?')

if cidade[0].find("SILVA") >= 0:
    print('Sim')
else:
    print('Não')
