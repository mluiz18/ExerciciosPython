# Escreva uma função que conte quantas vogais e consoantes existem em uma string.

def contador(string):
    c = 0
    v = 0
    text = string.upper().split()
    for i in range(len(text)):
        v_napalvra = 0
        c_napalavra = 0
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                if text[i][j] in "AEIOUÁÀÉÈÍÌÚÙÓÒÂÊÎÔÛ":
                    v_napalvra += 1
                else:
                    c_napalavra += 1
        c += c_napalavra
        v += v_napalvra
    return c, v


print(contador("Eu tenho 3 peixes"))