# Receba uma frase e inverta a ordem das palavras, não os caracteres.

def inversor_de_frase(frase):
    texto = frase.split()
    invertido = texto[::-1]
    return " ".join(invertido)

print(inversor_de_frase("Eu amo pudim!"))