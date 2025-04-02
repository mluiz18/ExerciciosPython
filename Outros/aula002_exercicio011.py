media = 0
idade_homem_mais_velho = 0
homem_mais_velho = ""
mulheres_menos_20 = 0

for x in range(0,4):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo: ")).title()
    media = idade + media

    if sexo == "H" or "Homem" or "M" or "Masculino":
        if idade > idade_homem_mais_velho:
            homem_mais_velho = nome

    if sexo == "M" or "Mulher" or "F" or "Feminino":
        if idade < 20:
            mulheres_menos_20 += 1

media = media/4

print(f"A Média de idade do grupo é {media}!")
print(f"O Homem mais velho é o {homem_mais_velho}!")
print(f"No total são {mulheres_menos_20} mulheres com menos de 20 anos!")