valor = float (input('Valor de sua compra R$'))
desc = 0
parc = 0
valorfinal = 0
print('''
=============== FORMAS DE PAGAMENTO ==========
[1] A vista no dinheiro
[2] A vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao
==============================================''')
r = int(input('Qual a opcao? '))

if r == 1:
    desc = valor*10 / 100
    valor = valor - desc
    print(F'Sua compra sera de R${valor:.2f}')
elif r == 2:
    desc = valor*5 / 100
    valor = valor - desc
    print(f'Sua compra sera de R${valor:.2f}')
elif r == 3:
    parc = valor/2
    print(f'Sua compra foi de R${valor:.2f}, Voce pagara em 2x de R${parc:.2f}')
elif r == 4:
    quantp = int(input('Quantas vazer voce ira parcelar? '))
    desc = valor *20 / 100
    valorfinal = valor + desc
    parc = valorfinal / quantp

    print(f'Sua compra sera parcelada em {quantp}x de R${parc:.2f} COM JUROS.')
    print(f'Sua compra de R${valor:.2f} vai custar R${valorfinal:.2f} no final')
print('Obrigado pela preferencia! Volte sempre!')