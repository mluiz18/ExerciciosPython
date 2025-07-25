palavra = "arara"

c = 0
tamanho = len(palavra)
e_palindromo = 0

for i in range(tamanho):
    if palavra[i] == palavra[tamanho-1]:
        e_palindromo += 1
    c += 1
    tamanho -= 1
    if e_palindromo > tamanho:
        print(f"A Palavra {palavra} é um palíndromo!")
        break
    else:
        if c == tamanho:
            print(f"A Palavra {palavra} NÃO é um palíndromo!")
            break