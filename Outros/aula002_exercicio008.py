frase = str(input("Digite a frase: ")).strip()
tamanho = len(frase)

for x in range(0,len(frase)):
    if frase[x] == frase[tamanho-1]:
        print(frase[x], frase[tamanho-1])
        tamanho = tamanho - 1