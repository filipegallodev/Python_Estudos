salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250.0:
    salario += (salario * (10 / 100))
else:
    salario += (salario * (15 / 100))

print(f'O novo salário com o aumento é de: R${salario}')
