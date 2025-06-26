c50 = 0
c20 = 0
c10 = 0
c1 = 0
soma = 0

valor = int(input("Digite o valor a ser sacado: R$"))
while True:
    if soma + 50 <= valor:
        soma += 50
        c50 += 1
    else:
        if soma + 20 <= valor:
            soma += 20
            c20 += 1
        else:
            if soma + 10 <= valor:
                soma += 10
                c10 += 1
            else:
                if soma + 1 <= valor:
                    soma += 1
                    c1 += 1

    if soma == valor:
        break

print(f"Total células de 50 = {c50}")
print(f"Total células de 20 = {c20}")
print(f"Total células de 10 = {c10}")
print(f"Total células de 1 = {c1}")
