def somar_matriz(matriz):
    soma_diagonal_principal = 0
    for i in range(len(matriz)):
        soma_diagonal_principal += matriz[i][i]

    soma_diagonal_secundaria = 0
    for i in range(len(matriz)):
        j = (len(matriz)-1)-i
        soma_diagonal_secundaria += matriz[i][j]

    return soma_diagonal_principal, soma_diagonal_secundaria


matriz = [
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
         ]

print(somar_matriz(matriz))