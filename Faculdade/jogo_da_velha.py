from random import *

def diagonal_principal(tabuleiro, jogador):
    contador = 0
    for i in range(3):
        if tabuleiro[i][i] == jogador:
            contador = contador + 1
    if contador == 3:
        return True
    return False

def diagonal_secundaria(tabuleiro, jogador):
    contador = 0
    for i in range(3):
        j = 2 - i
        if tabuleiro[i][j] == jogador:
            contador = contador + 1
    if contador == 3:
        return True
    return False

def linha_vencedora(tabuleiro, linha, jogador):
    contador = 0
    for coluna in range(3):
        if tabuleiro[linha][coluna] == jogador:
            contador = contador + 1
    if contador == 3:
        return True
    return False

def coluna_vencedora(tabuleiro, coluna, jogador):
    contador = 0
    for linha in range(3):
        if tabuleiro[linha][coluna] == jogador:
            contador = contador + 1
    if contador == 3:
        return True
    return False

def verificar_vitoria(tabuleiro, jogador):
    linha = 0
    while linha < 3:
        if linha_vencedora(tabuleiro, linha, jogador):
            return True
        if coluna_vencedora(tabuleiro, linha, jogador):
            return True
        linha = linha + 1
    if diagonal_principal(tabuleiro, jogador):
        return True
    if diagonal_secundaria(tabuleiro, jogador):
        return True
    return False

def posicoes_disponiveis(tabuleiro):
    livres = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] != "X" and tabuleiro[linha][coluna] != "O":
                livres.append((linha, coluna))
    return livres

def jogada_bot(tabuleiro,jogo):
    livres = posicoes_disponiveis(tabuleiro)

    for i in range(len(livres)):
        linha, coluna = livres[i]
        tabuleiro[linha][coluna] = "O"
        if verificar_vitoria(tabuleiro, "O"):
            return
        tabuleiro[linha][coluna] = " "

    for i in range(len(livres)):
        linha, coluna = livres[i]
        tabuleiro[linha][coluna] = "X"
        if verificar_vitoria(tabuleiro, "X"):
            tabuleiro[linha][coluna] = "O"
            return
        tabuleiro[linha][coluna] = " "

    if jogo:
        posicao_aleatoria = choice(livres)
        linha, coluna = posicao_aleatoria
        tabuleiro[linha][coluna] = "O"

def mostrar_tabuleiro(tabuleiro):
    for linha in range(3):
        linha_texto = f"{linha} "
        for coluna in range(3):
            linha_texto = linha_texto + tabuleiro[linha][coluna] + " "
        print(linha_texto)

def posicao_valida(numero):
    if numero < 0 or numero > 2:
        return False
    else:
        return True

tabuleiro = [
                [" "," "," "],
                [" "," "," "],
                [" "," "," "]
            ]
jogo_ativo = True
while jogo_ativo:
    print("  0 1 2")
    mostrar_tabuleiro(tabuleiro)
    linha = int(input("Escolha a linha: "))
    posicao_linha = posicao_valida(linha)
    coluna = int(input("Escolha a coluna: "))
    posicao_coluna = posicao_valida(coluna)

    if posicao_linha and posicao_coluna:
        while tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada, escolha outra.")
            linha = int(input("Escolha a linha: "))
            coluna = int(input("Escolha a coluna: "))

        tabuleiro[linha][coluna] = "X"

        if verificar_vitoria(tabuleiro, "X"):
            print("  0 1 2")
            mostrar_tabuleiro(tabuleiro)
            print("Parabéns! Você venceu!")
            jogo_ativo = False

        if len(posicoes_disponiveis(tabuleiro)) == 0:
            print("  0 1 2")
            mostrar_tabuleiro(tabuleiro)
            empate = True
            print("Empate!")
            jogo_ativo = False

        jogada_bot(tabuleiro,jogo_ativo)

        if verificar_vitoria(tabuleiro, "O"):
            if jogo_ativo:
                print("  0 1 2")
                mostrar_tabuleiro(tabuleiro)
                print("O bot venceu!")
                jogo_ativo = False

        if len(posicoes_disponiveis(tabuleiro)) == 0:
            if jogo_ativo:
                print("  0 1 2")
                mostrar_tabuleiro(tabuleiro)
                print("Empate!")
                jogo_ativo = False
    else:
        print("Posição Inválida, Jogue novamente!")