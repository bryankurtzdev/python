lista = []
for c in range(0, 3):
    for b in range(0, 3):
        lista.append(int(input(f'Digite um valor para a [{c}, {b}]: ')))
print(f'{lista[:1]} {lista[1:2]} {lista[2:3]}')
print(f'{lista[3:4]} {lista[4:5]} {lista[5:6]}')
print(f'{lista[6:7]} {lista[7:8]} {lista[8:9]}')
