print("-"* 50)
print("Sequência de Fibonacci")
print("-"* 50)

termos = int(input("Quantos termos você quer mostrar? "))

primeiro_numero = 0
segundo_numero = 1

c = 0

while c < termos:
    if c == 0:
        print(primeiro_numero)
        print(segundo_numero)
        c += 1
    else:
        terceiro_numero = primeiro_numero + segundo_numero
        print(terceiro_numero)
        primeiro_numero = segundo_numero
        segundo_numero = terceiro_numero
        c += 1