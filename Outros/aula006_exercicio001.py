valores = []
for x in range(5):
    valores.append(int(input("Digite um valor: ")))

menor = valores[0]
maior = valores[0]
for numero in range(len(valores)):
    if valores[numero] > maior:
        maior = valores[numero]
    else:
        if valores[numero] < menor:
            menor = valores[numero]

print(f"O Maior valor da lista é {maior}")
print(f"O Menor valor da lista é {menor}")