valores = [81,1,2,18,4,-2,-18,9]
menor = valores[1]

for i in range(len(valores)):
    if valores[i] < menor:
        menor = valores[i]

print(menor)