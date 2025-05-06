valores = [10, 0, -1, -3, 5, 8, -2, -4, 7, 9]

for i in range(len(valores)):
    for x in range(i, len(valores)):
        if valores[x] < valores[i]:
            aux = valores[x]
            valores[x] = valores[i]
            valores[i] = aux

print(valores)