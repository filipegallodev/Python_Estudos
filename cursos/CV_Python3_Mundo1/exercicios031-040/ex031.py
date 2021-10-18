distancia = float(input('Digite a distância em Km da viagem: '))

if distancia <= 200:
    distancia = distancia * 0.50
    print(f'O valor total a ser pago pela passagem é de R${distancia}')
else:
    distancia = distancia * 0.45
    print(f'O valor total a ser pago pela passagem é de R${distancia}')
