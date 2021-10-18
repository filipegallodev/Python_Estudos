import sys

numero = input('Digite um número entre 0 e 9999: ')

if int(numero) < 0 or int(numero) > 9999:
    print('Valor inválido! Encerrando ...')
    sys.exit()

print(f'Unidade: {numero[3]}')
if int(numero) >= 10:
    print(f'Dezena: {numero[2]}')

if int(numero) >= 100:
    print(f'Centena: {numero[1]}')

if int(numero) >= 1000:
    print(f'Milhar: {numero[0]}')
