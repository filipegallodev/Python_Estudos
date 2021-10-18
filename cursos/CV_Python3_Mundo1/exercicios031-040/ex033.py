num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print(f'O primeiro número ({num1}), é o maior')
    if num2 > num3:
        print(f'O terceiro número ({num3}), é o menor')
    else:
        print(f'O segundo número ({num2}), é o menor')
elif num2 > num3:
    print(f'O segundo número ({num2}), é o maior')
    if num1 > num3:
        print(f'O terceiro número ({num3}), é o menor')
    else:
        print(f'O primeiro número ({num1}), é o menor')
else:
    print(f'O terceiro número ({num3}), é o maior')
    if num2 > num1:
        print(f'O primeiro número ({num1}), é o menor')
    else:
        print(f'O segundo número ({num2}), é o menor')
