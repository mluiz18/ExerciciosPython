valores_negativos = 0
for i in range(10):
    valor = int(input("Digite um valor: "))
    if valor < 0:
        valores_negativos += 1

print(f"Ao todo são {valores_negativos} valores negativos!")