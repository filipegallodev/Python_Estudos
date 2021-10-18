dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km o carro rodou? '))

print(f'O valor a pagar pelo aluguel do carro é: R$ {dias * 60 + km * 0.15}')
