matriz = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
         ]

def somar_toda_a_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return soma

def somar_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

def somar_diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)):
        j = (len(matriz) - 1) - i
        soma += matriz[i][j]
    return soma

def somar_linha_matriz(matriz, line):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[line][i]
    return soma

def somar_coluna_matriz(matriz,koln):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][koln]
    return soma

linha = int(input("Qual linha quer somar? "))
coluna = int(input("Qual coluna quer somar? "))
print(somar_linha_matriz(matriz, linha))
print(somar_coluna_matriz(matriz, coluna))
print(somar_diagonal_principal(matriz))
print(somar_diagonal_secundaria(matriz))
print(somar_toda_a_matriz(matriz))
