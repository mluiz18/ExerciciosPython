valores = [81,1,2,18,4,-2,-18,9]
maior = valores[1]
for i in range(len(valores)):
    if valores[i] > maior:
        maior = valores[i]

print(maior)