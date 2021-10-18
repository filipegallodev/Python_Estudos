ladoA = int(input('Digite o tamanho do lado A: '))
ladoB = int(input('Digite o tamanho do lado B: '))
ladoC = int(input('Digite o tamanho do lado C: '))

if ladoA + ladoC > ladoB and ladoA + ladoB > ladoC and ladoB + ladoC > ladoA:
    print('É possível formar um triângulo com estas medidas!')
else:
    print('Com estas medidas não é possível formar um triângulo.')
