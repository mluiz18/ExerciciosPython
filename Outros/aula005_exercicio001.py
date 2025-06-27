def verificador_de_numero(n):
    if n < 0:
        return False
    if n > 20:
        return False
    return True

numero = int(input("Digite um número entre 0 e 20: "))
validade = verificador_de_numero(numero)
n = "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove", "vinte"

while not validade:
    print("Número inválido! Tente novamente.")
    numero = int(input("Digite um número entre 0 e 20: "))
    validade = verificador_de_numero(numero)

print(f"Você digitou o numero {n[numero]}")

