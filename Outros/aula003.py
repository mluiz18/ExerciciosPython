r = "S"
pares = []
p = 0
impares = []
i = 0

while r == "S":
    numero = int(input("Digite um número: "))
    if numero % 2 == 0 :
        pares.append(numero)
        p += 1
    else:
        impares.append(numero)
        i += 1
    r = str(input("Quer continuar? [S/N]: ")).title()

print(f"Você digitou {p} números pares, {i} número impares.")
ans = str(input("Deseja ver quais numéros pares ou impares você digitou? [S/N]: ")).upper()
if ans == "S":
    resp = str(input("Quer ver os número pares ou impares? [P/I]: ")).upper()
    if resp == "P":
        print(pares)
    else:
        if resp == "I":
            print(impares)
        else:
            print("Resposta inválida")