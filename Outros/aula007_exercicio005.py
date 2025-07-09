from time import sleep
from random import *
jogos = int(input("Quantos jogos quer gerar? "))
valores = []
numeros = []

r = 0
while r < jogos:
    c = 0
    while c < 6:
        numero = randint(1,60)
        if numero not in numeros:
            numeros.append(numero)
            c += 1
    numeros.sort()
    valores.append(numeros[:])
    numeros.clear()
    r += 1

print("-="*30)
print(" "*22, "Resultados")
print("-="*30)
for x in range(len(valores)):
    print(f"Jogo {x+1}: {valores[x]}")
    sleep(1)