matriz = [[],[],[]]
for i in range(3):
    for x in range(3):
        matriz[i].append(int(input(f"Digite um valor para a posição [{i},{x}]: ")))

print("-=" *10)
print("Matriz")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()