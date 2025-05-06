texto = str(input("Digite um texto: "))
char = str(input("Digite um caractere: "))
i = 0

while texto[i] != char:
    print(texto[i])
    i += 1
print(texto[i])