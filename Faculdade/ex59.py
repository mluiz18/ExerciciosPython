def primeiros_caracteres(string, caracter):
    resultado = ""
    i = 0
    while string[i] != caracter:
        resultado = resultado + string[i]
        i = i + 1
    resultado = resultado + string[i]
    return resultado

print(primeiros_caracteres("Monza Tubarão", "u"))