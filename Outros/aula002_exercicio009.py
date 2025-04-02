maiores_de_idade = 0
menores_de_idade = 0

for x in range(0,7):
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    if 2025 - ano_nascimento >= 18:
        maiores_de_idade += 1
    else:
        menores_de_idade += 1

print(f"Ao todo são {maiores_de_idade} maiores de idade, e {menores_de_idade} menores de idade")