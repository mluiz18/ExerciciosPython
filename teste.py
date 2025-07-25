palavra = "Renner"
palavra_invertida = palavra[::-1]
if palavra.upper() == palavra_invertida.upper():
    print("É palíndromo!")
else:
    print("Não é palíndromo!")