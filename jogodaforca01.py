palavra = str(input("Digite a sua palavra: ")).upper()
aux = []

for y in range(len(palavra)):
    aux.append(palavra[y])

print(" \n"*500)

print(["_"]*len(palavra))

palavra = ["_"] * len(aux)
c = 0
palavras_usadas = []
rodadas_gastas = 0

while c < 6:
    c = c + 1
    pode_verificar = True
    letra = str(input("Digite sua letra: ")).upper().strip()

    if c == 1:
        palavras_usadas.append(letra)
    else:
        for j in range(len(palavras_usadas)):
            if letra == palavras_usadas[j]:
                c = c - 1
                pode_verificar = False
                print("Letra ja usada!")
            else:
                palavras_usadas.append(letra)

    if pode_verificar:
        for i in range(len(aux)):
            if aux[i] == letra:
                palavra[i] = letra

    rodadas_gastas = c
    if palavra == aux:
        c = 6

    print(f"Rodada {rodadas_gastas} de 6")
    print(palavra)

if palavra == aux:
    print(f"Você venceu, com {rodadas_gastas} rodadas!")
else:
    print("Você perdeu!")
