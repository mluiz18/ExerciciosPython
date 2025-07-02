valores = []
resp = "S"

while resp != "N":
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? [S/N] ")).title()

print(f"Ao todo foram digitados {len(valores)} valores!")
valores.sort(reverse=True)
print(f"Os valores digitados de ordem decrescente: {valores}")

if 5 in valores:
    print("O Valor 5 está na lista!")
else:
    print("O Valor 5 não está na lista!")