from random import randint

lista = []
for i in range(10):
    lista.append(randint(0,18))
print(lista)

maior = lista[0]
menor = lista[0]
for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    else:
        if lista[i] < menor:
            menor = lista[i]

print(maior)
print(menor)