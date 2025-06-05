def retornar_menor_elemento_diagonal_secundaria(matriz):
    menor = matriz[0][5]
    for i in range(len(matriz)):
        j = (len(matriz)-1)-i
        if matriz[i][j] < menor:
            menor = matriz[i][j]
    return menor

matriz = [
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
         ]

menor = retornar_menor_elemento_diagonal_secundaria(matriz)
print(menor)