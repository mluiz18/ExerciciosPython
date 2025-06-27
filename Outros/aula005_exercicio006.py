palavras = "Python", "Computador", "Fortnite", "Programador", "Sexo"

for p in palavras:
    print(f"\n Na palavra {p}, temos ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end="")