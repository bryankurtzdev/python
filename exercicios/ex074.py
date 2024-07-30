from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print('OS valores sorteados foram: ', end=' ')
for c in num:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
