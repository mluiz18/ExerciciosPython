maior_valor = 0
menor_valor = 0

for i in range(5):
    valor = int(input("Digite um valor: "))
    if i == 1:
        maior_valor = valor
        menor_valor = valor
    else:
        if valor > maior_valor:
            maior_valor = valor
        else:
            if valor < menor_valor:
                menor_valor = valor

print(f"O Maior valor digitado foi {maior_valor}")
print(f"O Menor valor digitado foi {menor_valor}")