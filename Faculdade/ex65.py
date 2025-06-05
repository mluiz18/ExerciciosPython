def somar_matriz_nao_quadrada(matriz):
    soma_linha = 0
    for i in range(len(matriz)):
        soma_linha += matriz[4][i]

    soma_coluna = 0
    for i in range(len(matriz)):
        soma_coluna += matriz[i][2]

    return soma_linha,soma_coluna

matriz = [
          [1,2,3,4,5,6,0],
          [1,2,3,4,5,6,0],
          [1,2,3,4,5,6,0],
          [1,2,3,4,5,6,0],
          [1,2,3,4,5,6,0],
          [1,2,3,4,5,6,0],
          [1,2,3,4,5,6,0]
         ]

somas = somar_matriz_nao_quadrada(matriz)

print(somas)