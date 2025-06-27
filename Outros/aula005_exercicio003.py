from random import *

def maior_valor_gerado(n):
    maior = n[0]
    for i in range(len(n)):
        if n[i] > maior:
            maior = n[i]
    return maior

def menor_valor_gerado(n):
    menor = n[0]
    for i in range(len(n)):
        if n[i] < menor:
            menor = n[i]
    return menor

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)

numeros_aleatorias = n1, n2, n3, n4, n5
print(f"O Número gerados foram: {numeros_aleatorias}")
print(f"O Maior número gerado foi {maior_valor_gerado(numeros_aleatorias)}")
print(f"O Menor número gerado foi {menor_valor_gerado(numeros_aleatorias)}")