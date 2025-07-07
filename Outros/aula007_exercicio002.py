valores_totais = [[], []]

for i in range(7):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        valores_totais[0].append(valor)
    else:
        valores_totais[1].append(valor)

valores_totais[0].sort()
valores_totais[1].sort()

print(f"Valores pares: ", end="")
for i in range(len(valores_totais[0])):
    print(valores_totais[0][i], end=", ")
print()
print("Valores impares: ", end="")
for x in range(len(valores_totais[1])):
    print(valores_totais[1][x], end=", ")