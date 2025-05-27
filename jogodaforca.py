palavra = str(input("Digite a sua palavra: ")).upper()
aux = []

for y in range(len(palavra)):
    aux.append(palavra[y])

print(" \n"*500)

print(["_"]*len(palavra))

palavra = ["_"] * len(aux)
palavras_erradas = 0
palavras_usadas = []
rodadas_gastas = 1

def verificador(letra, aux, palavra):
    letra_achada = False
    for i in range(len(aux)):
        if aux[i] == letra:
            palavra[i] = letra
            letra_achada = True

    return letra_achada

while palavras_erradas < 6:
    pode_verificar = True
    letra = str(input("Digite sua letra: ")).upper().strip()

    if len(letra) > 1:
        print("Digite uma letra válida!")
    else:
        if letra.isnumeric():
            print("Digite uma letra válida!")
        else:
            i = 0
            while i < len(palavras_usadas):
                if letra == palavras_usadas[i]:
                    pode_verificar = False
                    i = len(palavras_usadas)
                else:
                    i = i + 1

            if pode_verificar:
                palavras_usadas.append(letra)
                letra_achada = verificador(letra, aux, palavra)

            if not letra_achada:
                palavras_erradas = palavras_erradas + 1

            if palavra == aux:
                palavras_erradas = 6

            rodadas_gastas = rodadas_gastas + 1

            print(f"Palavras erradas: {palavras_erradas}/6")
            print(f"Palavras Digitadas: {palavras_usadas}")
            print(palavra)

if palavra == aux:
    print(f"Você venceu, com {rodadas_gastas} rodadas!")
else:
    print("Você perdeu!")