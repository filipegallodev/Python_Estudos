from datetime import date

ano = int(input('Digite um ano qualquer (Coloque 0 para analisar o ano atual): '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print(f'{ano} não é um ano bissexto.')
    else:
        print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto')
