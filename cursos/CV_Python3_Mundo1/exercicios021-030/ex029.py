velocidade = int(input('Digite a velocidade do carro em Km/h: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de 80Km/h! Foi multado em R${multa}!')
