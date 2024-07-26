num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero entre 0 e 20: '))
if n < 0 or n > 20:
    while n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'O numero que voce digitou e {num[n]}')
