frase = str(input("Digite a frase: ")).strip().upper()
palavra = frase.split()
junto = "".join(palavra)
inverso = ""
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print(f"A Frase ao contrario é {inverso}")
if inverso == junto:
    print(f"A Frase {frase} é um palíndromo!")
else:
    print(f"A Frase {frase} NÃO é um palíndromo!")
