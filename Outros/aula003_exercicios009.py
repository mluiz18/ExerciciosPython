resp = "S"
soma = 0
c = 0
while resp == "S":
    numero = int(input("Digite um número: "))
    if c == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        else:
            if numero < menor:
                menor = numero
    soma += numero
    c += 1
    resp = str(input("Quer continuar? [S/N] ")).upper()

print(f"Você digitou {c} números")
print(f"A Média dos números é igual a {soma/c}")
print(f"O Maior número digitado foi {maior}")
print(f"O Menor número digitado foi {menor}")
