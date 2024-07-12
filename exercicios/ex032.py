from datetime import date
print('VERIFICADOR DE ANO BISSEXTO')
a = int(input('Que ano voce quer analisar? Digite 0 para analisar o ano atual: '))
if a == 0:
    a == date.today().year
print('=+=+='* 20)
if a %4 == 0 and a %100 != 0 or a %400 == 0:
    print(f'O ano {a} e BISSEXTO')
else:
    print(f"O ano {a} nao e BISSEXTO")