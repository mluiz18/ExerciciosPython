pessoas = []
dados = []
maior = menor = 0


while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input("Quer continuar? [S/N] "))
    if r in "NnNaonao":
        break

print(f"Foram cadastradas {len(pessoas)} pessoas!")
print(f"O Maior peso é {maior} de ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}, ", end="")
print()
print(f"O Menor peso é {menor} de ", end="")
for g in pessoas:
    if g[1] == menor:
        print(f"{g[0]}, ", end="")