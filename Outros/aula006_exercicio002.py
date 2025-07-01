valores = []
resp = "S"
while True:
    valor = int(input("Digite um valor: "))
    if not valor in valores:
        valores.append(valor)
    else:
        print("Valor repetido!")

    resp = str(input("Deseja continuar? [S/N] ")).title()
    if resp == "N":
        break
valores.sort()
print("-=" * 25)
print(f"Os valores digitados foram {valores}")