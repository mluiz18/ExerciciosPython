lista = []
for i in range(5):
    lista.append(int(input("Digite um número: ")))

for i in range(len(lista)):
    for j in range(i, len(lista)):
        if lista[i] > lista[j]:
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux

print(lista)