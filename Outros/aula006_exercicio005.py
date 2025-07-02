valores = []
valores_pares = []
valores_impares = []

while True:
    valor = int(input("Digite um valor: "))
    valores.append(valor)
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

    resp = str(input("Quer continuar? [S/N] ")).title()
    if resp[0] == "N":
        break

print("-="*50)
print(f"Os valores digitados foram: {valores}")
print(f"Os valores pares digitados foram: {valores_pares}")
print(f"Os valores impares digitados foram: {valores_impares}")