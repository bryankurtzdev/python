times = ("Flamengo", "Bahia", "Botafogo", "São Paulo", "Athletico-PR",
    "Red Bull Bragantino", "Palmeiras", "Internacional", "Cruzeiro",
    "Atlético-MG", "Fortaleza", "Juventude", "Grêmio", "Vasco",
    "Fluminense", "Criciúma", "Corinthians", "Atlético-GO", "Vitória",
    "Cuiabá")
print(f'Os 5 primeiros times do brasileirao sao {times[0:5]}')
print('---'*30)
print(f'Os 4 ultimos colocados na tabela sao {times[-4:]}')
print('---'*30)
print(f'Em ordem alfabetica a lista fica assim: {sorted(times)}')
print('---'*30)
print(f'O gremio se encontra na posicao {times.index("Grêmio")+1} da tabela')
