maior_peso = 0
menor_peso = 10000000

for x in range(0,5):
    peso = float(input("Digite seu peso: "))
    if peso > maior_peso:
        maior_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso

print(f"O Maior peso é: {maior_peso}Kg, e o menor peso é: {menor_peso}Kg")