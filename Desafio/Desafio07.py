#contar vogais

txt = "Eu amo café"
frase = txt.upper().split()
v = 0
print(frase)
for i in range(len(frase)):
    for j in range(len(frase[i])):
        if frase[i][j] in "AEIOUÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛ":
            v += 1

print(v)
