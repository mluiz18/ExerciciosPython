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

print("-="*3, "RESULTADOS", "-="*3)
print(f"1º Lugar: {geral[0][1]} com {geral[0][0]}")
print(f"2º Lugar: {geral[1][1]} com {geral[1][0]}")
print(f"3º Lugar: {geral[2][1]} com {geral[2][0]}")
print(f"4º Lugar: {geral[3][1]} com {geral[3][0]}")

