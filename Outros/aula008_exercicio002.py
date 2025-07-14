from random import *
from time import sleep
jogadas = {}
valores = []
geral = []
for i in range(4):
    jogadas[f"jogador {i}"] = randint(1,6)
    valores.append(jogadas[f"jogador {i}"])
    valores.append(f"jogador {i}")
    geral.append(valores[:])
    valores.clear()
geral.sort(reverse=True)
c = 0
while c < len(jogadas):
    print(f"Jogador {c}: {jogadas[f'jogador {c}']}")
    c+=1
    sleep(1)

print("-="*3, "RESULTADOS", "=-"*3)

for x in range(4):
    print(f"{x+1}º Lugar: {geral[x][1]} com {geral[x][0]}")


