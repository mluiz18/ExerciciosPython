def primeiros_caracteres(string, valor):
    resultado = ""
    if valor > len(string):
        valor = len(string)
    for i in range(valor):
        resultado = resultado + string[i]
    return resultado

print(primeiros_caracteres("Might", 3))