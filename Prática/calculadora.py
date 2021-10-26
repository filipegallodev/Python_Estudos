print('-=-' * 13)
print('Seja bem-vindo à Super Calculadora 1.0!')
print('-=-' * 13)

condicional = 1

while condicional == 1:
    valorUm = float(input('Por favor, digite o primeiro valor que deseja realizar a operação: '))
    valorDois = float(input('Agora, o segundo valor: '))
    
    operador = input('Muito bem, agora digite o operador a ser utilizado ( +: adição, =: subtração, *: multiplicação , /: divisão ): ')
    if operador == '+':
        print(f'A soma entre {valorUm} e {valorDois} é: {valorUm + valorDois}')
    elif operador == '-':
        print(f'A soma entre {valorUm} e {valorDois} é: {valorUm - valorDois}')
    elif operador == '*':
        print(f'A soma entre {valorUm} e {valorDois} é: {valorUm * valorDois}')
    elif operador == '/':
        print(f'A soma entre {valorUm} e {valorDois} é: {valorUm / valorDois}')
    else:
        print('Erro!!! O operador inserido é inválido! Por favor, insira um operador válido.')

    condicional = int(input('Deseja realizar outra operação? 1 = Sim ou 0 = Não: '))

print('-=-' * 22)
print('Encerrando... Muito obrigado por utilizar a Super Calculadora 1.0!')
print('-=-' * 22)
