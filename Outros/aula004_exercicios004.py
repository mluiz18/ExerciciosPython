maior_de_idade = 0
homens = 0
mulheresmenos20 = 0

while True:
    idade = int(input("Digite a Idade: "))
    sexo = str(input("Digite o Sexo [H/M]: ")).upper()

    if idade >= 18:
        maior_de_idade += 1

    if sexo == "H":
        homens += 1

    if sexo == "M":
        if idade < 20:
            mulheresmenos20 += 1

    continuar = str(input("Quer continuar? [S/N]: ")).upper()
    if continuar == "N":
        break

print(f"Pessoas com mais de 18 anos = {maior_de_idade}")
print(f"Pessoas do sexo masculino = {homens}")
print(f"Mulheres com menos de 20 anos = {mulheresmenos20}")