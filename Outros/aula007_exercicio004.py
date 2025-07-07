matriz = [[],[],[]]
soma_par = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0

for i in range(3):
    for x in range(3):
        val = int(input(f"Digite um valor para a posição [{i},{x}]: "))
        matriz[i].append(val)
        if val % 2 == 0:
            soma_par += val
        if x == 2:
            soma_terceira_coluna += val
        if i == 1:
            if x == 0:
                maior_valor_segunda_linha = matriz[1][0]
            else:
                if val > maior_valor_segunda_linha:
                    maior_valor_segunda_linha = val


print("-=" *10)
print("Matriz")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()

print(f"A soma de todos os valores pares: {soma_par}")
print(f"A soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"O maior valor da segunda linha: {maior_valor_segunda_linha}")