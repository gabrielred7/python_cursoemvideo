jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
for c in range(0+1, tot+1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*10)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*10)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')