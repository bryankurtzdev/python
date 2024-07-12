from datetime import date
ano = date.today().year
nas = int(input('Qual ano voce nasceu? '))
idd = ano - nas
print(f'O atleta tem {idd} anos.')
if idd < 9:
    print('Voce pertence a categoria MIRIM')
elif idd <= 14:
    print('Voce pertence a categoria INFANTIL')
elif idd <= 19:
    print('Voce pertence a categoria JUNIOR')
elif idd <= 25:
    print('Voce pertence a categoria SENIOR')
else:
    print('Voce pertence a categoria MASTER')