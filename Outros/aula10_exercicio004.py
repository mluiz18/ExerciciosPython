def leiaint(n):
    while not n.isnumeric():
        print("ERRO! Digite um número inteiro válido!")
        n = input("Digite um número: ")

    if n.isnumeric():
        return n

numero = leiaint(input("Digite um número: "))
print(f"Você digitou o número {numero}")
