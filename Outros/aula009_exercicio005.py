from random import randint
from time import sleep

def sortear(lista):
    for i in range(5):
        lista.append(randint(0,10))

    return lista

def soma_par(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            soma += lista[i]
    return soma

numero = []
numero = sortear(numero)
print("-="*3, "SORTEANDO 5 VALORES", "=-"*3)
for n in numero:
    print(n, end=" ")
    sleep(0.5)
print()
print(f"A Soma dos valores pares gerados é {soma_par(numero)}")
