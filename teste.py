string = "Mazda"
texto = string.upper().split()

c = 0
for p in texto:
    for i in range(len(p)):
        if p[i].isalpha():
            if p[i] in "AEIOUÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛ":
                c += 1

print(f"Na frase '{string}'. Temos ao todo {c} vogais.")