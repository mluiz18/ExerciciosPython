soma_valor = 0
quantidade_valor = 0
valores_positivos = 0
valores_negativos = 0
valor = int(input("Digite um valor: "))

while valor != 0:
    soma_valor += valor
    quantidade_valor += 1
    if valor > 0:
        valores_positivos += 1
    if valor < 0:
        valores_negativos += 1
    valor = int(input("Digite um valor: "))

print(f"A Média dos números é {soma_valor/quantidade_valor}")
print(f"A Quantidade de números negativos é {valores_negativos}")
print(f"A Quantidade de números positivos é {valores_positivos}")
print(f"O Percentual de valores negativos é {(valores_negativos*quantidade_valor)/100}")
print(f"O Percentual de valores positivos é {(valores_positivos*quantidade_valor)/100}")